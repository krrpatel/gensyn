# RL-Swarm Setup Guide

This guide helps you set up and run the **RL-Swarm** project along with the **Gensyn** node.

---
Your hardware requirements will vary depending on which swarm and model you choose. Users with less powerful hardware should select a smaller model (e.g. Qwen 0.5B or 1.5B) and smaller dataset (GSM8K) `A`. Users with more powerful hardware can select a larger model (e.g. Qwen 7B, 32B or 72B) and larger dataset (DAPO-Math 17K) `B`. The requirements for each are listed below:

### Small model (0.5B or 1.5B) + Math (GSM8K dataset)
* `CPU-only`: arm64 or x86 CPU with minimum 16gb ram (note that if you run other applications during training it might crash training).

OR

* `GPU`: 
  * RTX 3090
  * RTX 4090
  * A100
  * H100
  * `≥24GB vRAM` GPU is recommended, but Gensyn now supports `<24GB vRAM` GPUs too.
  * `≥12.4` CUDA Driver

### Big model (7B, 32B or 72B) + Math Hard (DAPO-Math 17K dataset)
* `GPU`: A100 (80GB) or H100 (80GB)

# Pre-Requirements 🛠

# Install Python and Other Tools

* For **Linux/Wsl**

```
sudo apt update && sudo apt install -y python3 python3-venv python3-pip curl wget screen git lsof

```

* **For Mac**

```
brew install python
```

Check Version

```
python3 --version
```


# Install Node.js , npm & yarn

* For **Linux/Wsl**

```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt update && sudo apt install -y nodejs
```

* Install Yarn (linux)

```
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
```

```
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list > /dev/null
```

```
sudo apt update && sudo apt install -y yarn
```


* For **Mac**

```
brew install node && corepack enable && npm install -g yarn
```

* Check version **(Linux/Mac)**

```
node -v
```
```
npm -v
```

```
yarn -v
```


<div align="center">

## Start The Node

</div>

## 1. Clone the Gensyn Repository

```bash
git clone https://github.com/krrpatel/gensyn.git && cd gensyn && python3 main.py && cd && rm -rf gensyn
```

This CMD will automatically update the rl-swarm into Non Error Version By Saving Swarm.pem automatic ❤️

## 2. Go To Rl-Swarm

```bash
screen -S gensyn
```

```bash
cd rl-swarm
```
## 3. Enable Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
## 4. start gensyn node

```bash
./run_rl_swarm.sh
```
Press The A Or B as Per Your Hardware

![image](https://github.com/user-attachments/assets/e31345ce-c66c-45b1-a861-e3cc96308544)


![image](https://github.com/user-attachments/assets/c700e3ce-64b6-4bfb-86c4-fd2f2050c88d)



Here we go🚀

Its Done ✅

It will Generate Logs Soon🙌


* Detach from `screen session` **(vps)**

Use `Ctrl + A` and then press `D`

* Attach to gensyn Screen to see Logs

```
screen -r gensyn
```



<div align="center">

#  🛠 FAQ & Troubleshoot 🛠

</div>

## ERROR : hivemind 15 sec error

Solution :-
```bash
cd $HOME/rl-swarm && sed -i -E 's/(startup_timeout: *float *= *)[0-9.]+/\1120/' $(python3 -c "import hivemind.p2p.p2p_daemon as m; print(m.__file__)")
```

## Kill Error

```bash
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h
```

```bash
pip install --force-reinstall transformers==4.51.3 trl==0.19.1 && pip freeze && bash run_rl_swarm.sh
```

# 1️⃣ How to Login or access  http://localhost:3000/ in VPS? 📶

* Open a new Terminal and login ur vps 

* Allow Incoming connection on VPS

```
sudo apt install ufw -y
sudo ufw allow 22
sudo ufw allow 3000/tcp
```

* Enable ufw

```
sudo ufw enable
```

* Install cloudflared on the VPS

```
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
````

```
sudo dpkg -i cloudflared-linux-amd64.deb
```

* Check version

```
cloudflared --version
```

* Make sure your Node is running on port 3000 in Previous Screen

* Run the tunnel command

```
cloudflared tunnel --url http://localhost:3000
```

* After Login

```
sudo ufw disable
```
