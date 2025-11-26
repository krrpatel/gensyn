
  
# ⚙️ 1. Requirements

- Ubuntu or WSL
- Python 3.10+
- SSH access to VPS
- 12GB RAM
- 50GB storage

---

# 🚀 2. Installation Steps

> **NOTE - I am Using Google cloud service for running CodeAssist & starting a SSH connection through my WSL**
### Step 1️⃣: Generate SSH Key in WSL

```bash
ssh-keygen -t ed25519 -C "codeassist"
```

**If you’re using other VPS providers, use `root` instead of "codeassist".**

- After running the above command in WSL, press Enter three times (ignore the passphrase line). Then use the command below to retrieve your SSH key: 

```bash
cat ~/.ssh/id_ed25519.pub
```

Save your SSH key in a notepad and create your VPS using this WSL SSH key.

> **NOTE - If you’re using Google Cloud, set your username to `codeassist`.**
> If you already possess a VPS and are encountering difficulties adding your WSL's SSH public key, please utilize the following command.

```bash
nano ~/.ssh/authorized_keys
```

- Once you've run that command, just paste your SSH key. Then hit Ctrl + O, press Enter, and finally, Ctrl + X.

---

### Step 2️⃣: Connect WSL to VPS

```bash
ssh -i ~/.ssh/id_ed25519 username@<your_external_ip>
```

- As mentioned earlier, use `codeassist` for GCP or `root` for other VPS providers. After executing the command, enter your VPS password if you are on on another vps.
Your WSL is now connected to your VPS.

---

### Step 3️⃣: Install Docker & Python

```bash
sudo apt update && sudo apt install docker.io git -y
sudo systemctl enable docker
sudo systemctl start docker
```

```bash
sudo apt install python3 python3-venv python3-pip curl -y
```

---

### Step 4️⃣: Clone Repository & Install UV

```bash
git clone https://github.com/gensyn-ai/codeassist.git
```

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

### Step 5️⃣: Run the CodeAssist

```
screen -S codeassist
```

```bash
cd codeassist
source .venv/bin/activate
uv run run.py
```

- **NOTE - After running this command, you’ll need to paste your Hugging Face token.
Generate one with `Write` access at [HUGGING FACE](https://huggingface.co/docs/hub/en/security-tokens)**

  ---
  
### Step 6️⃣: Create SSH Tunnel

- After entering your Hugging Face token, wait for the setup process to complete.
Then open a new WSL terminal tab and run: 

```bash
ssh -i ~/.ssh/id_ed25519 -f -N \
  -L 3000:localhost:3000 \
  -L 8000:localhost:8000 \
  -L 8001:localhost:8001 \
  -L 8008:localhost:8008 \
  username@<your_external_ip>
```

- **Replace username and ip with your VPS details.**
- **Now open your browser and go to http://localhost:3000/**
- **You can now log in to CodeAssist without any errors.**
  
- **LFG! Solve your problems ASAP ⚡**
️
---

  ### Step 7️⃣: Complete Your Training

  - **When you’re done coding, go to terminal (1) in WSL and press:
`CTRL` + `C`
This uploads your training data.**

---

# ♻️3. Restarting the service

 1️⃣. **IN WSL TERIMINAL #1**

 ```bash
ssh -i ~/.ssh/id_ed25519 username@<your_external_ip>
```

 2️⃣. **IN WSL TERMINAL #1** 

 ```
screen -r codeassist
```
 
```bash
cd codeassist
source .venv/bin/activate
uv run run.py
```

 3️⃣. **IN WSL TERMINAL #2**

```bash
ssh -i ~/.ssh/id_ed25519 -f -N \
  -L 3000:localhost:3000 \
  -L 8000:localhost:8000 \
  -L 8001:localhost:8001 \
  -L 8008:localhost:8008 \
  username@<your_external_ip>
```

-  **Run the above command just like in [Step 6️⃣](https://github.com/Suyashi3o/CodeAssist-Setup-Guide?tab=readme-ov-file#step-6%EF%B8%8F%E2%83%A3-create-ssh-tunnel), and you’re good to go.**

---

# 🧑‍💻4. RL-Swarm + CodeAssist on One VPS

1️⃣. **Update ports in CodeAssist**

```bash
  sed -i '0,/11434/s//11435/' compose.yml
sed -i -e 's/"11434\/tcp": 11434/"11434\/tcp": 11435/' -e 's#http://localhost:11434#http://localhost:11435#' run.py
```

2️⃣. **Update port in Web-UI Simulator**

```bash
cd web-ui/src/simulation/simulators
sed -i 's#http://localhost:11434#http://localhost:11435#' OllamaCodeSimulator.ts
```

3️⃣. **Run CodeAssist on new port**

```bash
cd ~/codeassist
uv run run.py --port 3001
```

4️⃣. **SSH tunnel for port 3001**

- **Use this command in wsl terminal.**

```bash
ssh -i ~/.ssh/id_ed25519 -f -N \
  -L 3001:localhost:3001 \
  -L 8000:localhost:8000 \
  -L 8001:localhost:8001 \
  -L 8008:localhost:8008 \
  username@<your_external_ip>
```

> NOTE - Since we're using port 3001 for CodeAssist, you'll need to go to this URL: http://localhost:3001 in your browser.Now enjoy login & solve problems ASAP !

5️⃣. **Want to restart again**

- **It'll all be just like before**
- **also remember this restart only for [POINT 4](https://github.com/Suyashi3o/CodeAssist-Setup-Guide?tab=readme-ov-file#%E2%80%8D4-rl-swarm--codeassist-on-one-vps)**

**1. IN VPS SCREEN**
 
```bash
cd codeassist
uv run run.py --port 3001
```

**2. IN WSL TERMINAL**
 
```bash
ssh -i ~/.ssh/id_ed25519 -f -N \
  -L 3001:localhost:3001 \
  -L 8000:localhost:8000 \
  -L 8001:localhost:8001 \
  -L 8008:localhost:8008 \
  username@<your_external_ip>
```

---


**Thank you 🙏**
              
