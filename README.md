# RL-Swarm Setup Guide

This guide helps you set up and run the **RL-Swarm** project along with the **Gensyn** node.

---

## 1. Clone the Gensyn Repository

```bash
git clone https://github.com/krrpatel/gensyn.git && python3 main.py && cd && rm -rf gensyn
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

