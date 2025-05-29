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

print("Done.")
