# RL-Swarm Setup Guide

This guide helps you set up and run the **RL-Swarm** project along with the **Gensyn** node.


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
Press N if you dont want to upload model to huggingface
then enter for default model traning


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

## auto shutdown / kill error

1. ctrl + c

2.
```bash
rm -f /tmp/hivemind-p2pd-*.sock && export P2P_CONTROL_PATH="/tmp/hivemind-p2pd-new.sock"
```
3. close current gensyn screen and make new screen by
```bash
screen -S gensyn
```

4. run swarm
```bash
cd rl-swarm && python3 -m venv .venv
source .venv/bin/activate && ./run_rl_swarm.sh
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
