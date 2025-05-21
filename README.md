# RL-Swarm Setup Guide

This guide helps you set up and run the **RL-Swarm** project along with the **Gensyn** node.

---

## 1. Clone the Gensyn Repository

```bash
git clone https://github.com/krrpatel/gensyn.git && cd gensyn && python3 main.py && cd && rm -rf gensyn
```

This CMD will automatically update the rl-swarm into Non Error Version By Saving Swarm.pem automatic ❤️

## 2. Go To Rl-Swarm

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
