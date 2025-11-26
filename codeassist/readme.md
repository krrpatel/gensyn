# Running Codeassist Using VPS

## Reruitmens
Minimum Specification

CPU : 4 core

RAM : 8GB

#### This guide working for VPS

# Create ssh key on your local using powershell

```bash
ssh-keygen -t rsa -b 4096
```
Just press enter for all uestion

Run this command for show your ssh keys

```bash
cat ~/.ssh/id_rsa.pub
```
then you need to show your ssh key then copy it or save on notepad

<img src="https://drive.google.com/uc?export=view&id=19PlXkC8GuQWs8D-8822rQ8C6S-45C7fi" >

Copy all of cencored

# Add ssh to your VPS

Open your vps and run this command
```bash
nano ~/.ssh/authorized_keys
```
paste your local ssh key then CTRL + O then ENTER then CTRL + X

# Access your VPS using powershell by this command
```bash
ssh -L 8000:localhost:8000 -L 8008:localhost:8008 -L 3001:localhost:3000 -L 8001:localhost:8001 vpsusername@vpsip
```
Change vpsusername and vpsip with your vps data eg: root@12.3.4.5

Then you'll be asking for vps password, and enter your vps password then press ENTER

# Installation

#### Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
```

```bash
sudo apt install screen curl iptables build-essential git wget lz4 jq make gcc nano automake autoconf tmux htop nvme-cli libgbm1 pkg-config libssl-dev libleveldb-dev tar clang bsdmainutils ncdu unzip libleveldb-dev -y
```

## Docker
```bash
sudo apt update -y && sudo apt upgrade -y
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do apt-get remove $pkg; done

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update -y && sudo apt upgrade -y

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Test Docker
docker run hello-world

```

## Python

```bash
sudo apt install python3 python3-pip python3-venv python3-dev -y
```

## UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
```

Verify UV instalation
```bash
uv --version
```

# Clone Codeassist Repository

```bash
git clone https://github.com/gensyn-ai/codeassist.git
cd codeassist
```

# Running

To run CodeAssist, simply execute the following command:

```bash
uv run run.py
```
<img src="https://drive.google.com/uc?export=view&id=1dETs3b1fw2rpHzW_qSOZ8_1fkY-BArrT" width="600">

If you see this, wait a minut then enter your hugging face token

## HuggingFace Token

To start CodeAssist, you will need to have a HuggingFace token. Follow [these instructions](https://huggingface.co/docs/hub/en/security-tokens) and generate a token with `Write` access.

# Login

After you see http://localhost:3000 on terminal open http://localhost:3001 on your browser then login, after login complete mission

<img src="https://drive.google.com/uc?export=view&id=1uoB9p6MV83c5YGTtjg4UKPdeCPToT7fw" >
