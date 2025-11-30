# codeassit-guide-for-VPS-users
## Hardware Requirements 
- **RAM**: 12GB+  
- **Disk**: 10GB+ SSD
  
> 💡 Tip: You can check [servarica.com](https://servarica.com) for affordable servers.

## 1. Prerequisites  

### Update packages
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

### Install dependencies
```bash
sudo apt install curl iptables build-essential git wget lz4 jq make gcc nano automake autoconf tmux htop nvme-cli libgbm1 pkg-config libssl-dev libleveldb-dev tar clang bsdmainutils ncdu unzip ufw screen gawk -y
```

### Install Docker
```bash
sudo apt update -y && sudo apt upgrade -y
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update -y && sudo apt upgrade -y
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Test Docker
sudo docker run hello-world

sudo systemctl enable docker
sudo systemctl restart docker
```

---

## 2. Install UV
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```bash
echo 'export PATH=$PATH:/root/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

## 3. Clone the repo and Go into directory
```bash
git clone https://github.com/gensyn-ai/codeassist.git
```
```bash
cd codeassist
```

### now to start the node, you'll need huggingface token with write permission
- **Go to `https://huggingface.co/` and create account if you currently don't have one**
- **Click profile photo by top right, click access tokens**
  
  <img width="1440" height="779" alt="image" src="https://github.com/user-attachments/assets/8bdc20d0-de95-41ab-96d3-07a1e2c8bfa4" />
  
- Now click create new token, select write, input any name and create
  
<img width="1009" height="469" alt="image" src="https://github.com/user-attachments/assets/098b1991-a682-4a79-b3ed-50e130a844dd" />

- copy the token and save it somewhere

## 4. Enter this command in your directory to run codeassist 
```bash
uv run run.py
```

### And if you are running rl-swarm on same VPS or PC, then follow these steps and run this with a different port flag, i.e

- i
```bash
  sed -i '0,/11434/s//11435/' compose.yml
sed -i -e 's/"11434\/tcp": 11434/"11434\/tcp": 11435/' -e 's#http://localhost:11434#http://localhost:11435#' run.py
```
- ii
```bash
cd web-ui/src/simulation/simulators
```
```bash
sed -i 's#http://localhost:11434#http://localhost:11435#' OllamaCodeSimulator.ts
```
```bash
cd && cd codeassist
```
```bash
uv run run.py --port 3001
```

**it,ll ask for your huggingface token, enter the access token you created and let it build**

**takes a couple of minutes to set up the containers so be patient**

<img width="915" height="652" alt="image" src="https://github.com/user-attachments/assets/b17cd961-c42b-436f-a74c-b7bc5e36851f" />

**take note of this, nothing will be shown when you paste huggingface token**


**Once it gets here and asks you to open url on browser, you'll need to forward ports over SSH(see step 5)*

<img width="963" height="641" alt="image" src="https://github.com/user-attachments/assets/9fbce663-bbe9-48ef-88ce-566dc41f378c" />

## 5. Forward ports over SSH
- If you are on window or Mac, open WSL (FOR WINDOWS) and Terminal (for mac) and paste this:
  ```bash
  ssh -L 8000:localhost:8000 -L 8008:localhost:8008 -L 3000:localhost:3000 -L 8001:localhost:8001 yourVPSusername@yourVPSIP
  ```
  **If you are running it with port 3001 then change 3000 to 3001 before forwarding in your WSL or Terminal**
  
  **Replace `yourVPSusername` with the actual one for your VPS**
  
  **Replace `yourVPSIP` with your VPS ip address
  
- example:
  
  <img width="1280" height="441" alt="image" src="https://github.com/user-attachments/assets/202ab744-ec79-4de5-b573-cc3029896a50" />

  **You'll see `Are you sure you want to continue connecting (yes/no/[fingerprint])?` type `yes`**
  **enter your VPS password when prompt for password**
  
  - you should now see something like this:
 ![IMG_7077](https://github.com/user-attachments/assets/08484943-d8eb-43b7-9d57-054e0ff89218)

## 6. Open *http://localhost:3000* or *http://localhost:3001* in your browser. depending on the port used

### Alternatively you can use localtunnel
**Open another tab of your VPS and run:**

```bash
sudo npm install -g localtunnel && lt --port 3000
```
**Change 3000 to 3001 if thats the port you run codeassist on.**

![telegram-cloud-photo-size-4-5805248209151003480-y](https://github.com/user-attachments/assets/04c31b01-43ee-476c-8fcd-ea0fe1fbf624)

**By your left is the problem, solve it on your right and use the submit solution button**

**try to submit at least 2 to 3 solution and don't just copy paste directly from anywhere**

![telegram-cloud-photo-size-4-5805248209151003498-y](https://github.com/user-attachments/assets/8f9d3031-61e5-44e1-ab5c-c1a927c23415)


### After submitting some solution, go back to your VPS and use ctrl c then wait for your model to be uploaded to HF

![telegram-cloud-photo-size-4-5805248209151003500-y](https://github.com/user-attachments/assets/926075d0-f351-49cd-97f4-77e686991494)

**Done, you can track your points on dashboard by sighning in with same email and OTP**




    
