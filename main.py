import os
import shutil
import subprocess

# Define paths
home = os.path.expanduser("~")
rl_swarm_dir = os.path.join(home, "rl-swarm")
swarm_pem_file = os.path.join(rl_swarm_dir, "swarm.pem")
home_swarm_pem = os.path.join(home, "swarm.pem")

# Step 1: Check if $HOME/rl-swarm exists
if os.path.exists(rl_swarm_dir):
    print("rl-swarm directory exists.")

    # Step 2: Check if swarm.pem exists inside rl-swarm
    if os.path.isfile(swarm_pem_file):
        print("swarm.pem found in rl-swarm. Moving to $HOME...")
        shutil.move(swarm_pem_file, home_swarm_pem)

    # Step 3: Remove rl-swarm directory
    print("Removing existing rl-swarm directory...")
    shutil.rmtree(rl_swarm_dir)

# Step 4: Clone the GitHub repo
print("Cloning rl-swarm repository...")
subprocess.run(["git", "clone", "https://github.com/gensyn-ai/rl-swarm.git"], cwd=home)

# Step 5: Move swarm.pem back into rl-swarm if it exists in $HOME
if os.path.isfile(home_swarm_pem):
    print("Moving swarm.pem back into rl-swarm...")
    shutil.move(home_swarm_pem, os.path.join(rl_swarm_dir, "swarm.pem"))

# Step 6: Run sed command to edit YAML
yaml_file = os.path.join(rl_swarm_dir, "hivemind_exp", "configs", "mac", "grpo-qwen-2.5-0.5b-deepseek-r1.yaml")
sed_cmd_yaml = (
    f"sed -i '"
    f"s/^torch_dtype: .*/torch_dtype: float32/; "
    f"s/^bf16: .*/bf16: false/; "
    f"s/^tf32: .*/tf32: false/; "
    f"s/^per_device_train_batch_size: .*/per_device_train_batch_size: 1/; "
    f"s/^gradient_checkpointing: .*/gradient_checkpointing: false/"
    f"' {yaml_file}"
)
print("Running sed command to edit YAML config...")
subprocess.run(sed_cmd_yaml, shell=True)

# Step 7: Run sed command to patch Python DHT call
grpo_runner_path = os.path.join(rl_swarm_dir, "hivemind_exp", "runner", "grpo_runner.py")
sed_cmd_py = (
    f"sed -z -i.bak 's/\\(hivemind\\.DHT([^)]*\\))/\\1, ensure_bootstrap_success=False)/' {grpo_runner_path}"
)
print("Patching grpo_runner.py to add ensure_bootstrap_success=False...")
subprocess.run(sed_cmd_py, shell=True)

print("Done.")
