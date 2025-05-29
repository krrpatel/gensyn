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

# Step 6: Run sed command to edit YAML config
yaml_file = os.path.join(rl_swarm_dir, "hivemind_exp", "configs", "mac", "grpo-qwen-2.5-0.5b-deepseek-r1.yaml")
sed_yaml_cmd = (
    f"sed -i '"
    f"s/^torch_dtype: .*/torch_dtype: float32/; "
    f"s/^bf16: .*/bf16: false/; "
    f"s/^tf32: .*/tf32: false/; "
    f"s/^per_device_train_batch_size: .*/per_device_train_batch_size: 1/; "
    f"s/^gradient_checkpointing: .*/gradient_checkpointing: false/"
    f"' {yaml_file}"
)
print("Running sed command to edit YAML config...")
subprocess.run(sed_yaml_cmd, shell=True)

# Step 7: Insert ensure_bootstrap_success=False into grpo_runner.py
runner_file = os.path.join(rl_swarm_dir, "hivemind_exp", "runner", "grpo_runner.py")
sed_runner_cmd = (
    "sed -i 's/\\*\\*self\\._dht_kwargs(grpo_args)/"
    "ensure_bootstrap_success=False, **self._dht_kwargs(grpo_args)/' "
    + runner_file
)
print("Running sed command to edit grpo_runner.py...")
subprocess.run(sed_runner_cmd, shell=True)

print("All tasks completed successfully.")
