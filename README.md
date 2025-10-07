# 🔎 st-find — Multi Social Media Username Checker ⚡

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Version-2.0-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Creator-satan-red?style=flat-square">
</p>

---

### ⚡ What’s this?
`st-find` is a **multi-platform username availability checker** 🧠  
It scans over **100+ social media networks, games, and platforms**  
to see if your name is **available or already taken** 👤  

> Works on Termux, Linux, macOS, and any system with Python 3 💻

---

## 🚀 Features

✅ Checks availability across **100+ networks**  
✅ Supports **socials + gaming platforms** (TikTok, Instagram, Fortnite, Roblox, etc.)  
✅ Fast, clean & colorful terminal output 💅  
✅ Auto installer with all required packages ⚙️  
✅ Perfect for brand checking, name hunting, or OG sniping 😈

---

## ⚙️ Setup Tutorial (Gen Z friendly version 😎)

### 🧩 Step 1: Clone the repo

```bash
git clone https://github.com/yourusername/st-find.git
cd st-find
```
💽 Step 2: Run setup wizard

This installs all dependencies (lolcat, requests, termcolor, etc.)
```
python setup.py
```
> 👀 Hit Y when asked — it’ll auto install 15+ required packages with pip/pkg!




---

🔥 Step 3: Start the scanner
```
python st-find.py
```
✨ Step 4: Enter your username

Example:

Enter the username to check (no @): satane

Then it’ll automatically scan TikTok, Instagram, YouTube, Steam, Twitch, Discord, and more ⚡
and show you whether the username is taken ❌ or available ✅.


---

💡 Example Output

[21:30:44] [INFO] [=] Starting scan for "satane" across 100 networks...
[21:30:45] [INFO] [+] Name available "satane (GitHub)"
[21:30:46] [INFO] [-] Name taken "satane (Instagram)"
[21:30:47] [INFO] [+] Name available "satane (Steam)"
[21:30:48] [INFO] Checks finished.


---

🧰 Requirements

🐍 Python 3.8+

💻 Internet connection

Optional: lolcat, figlet for colored banners


If you’re on Termux, everything installs automatically with:

pkg install python git -y


---

🧠 How It Works

The script loops through a list of 100+ social networks.

For each one, it tries to access your username’s profile URL.

If it returns a 404, it’s available ✅
If it returns a 200, it’s taken ❌

It handles redirects, errors, and rate limits gracefully.



---

🎨 Tech Stack

Python 3

requests

termcolor / colorama

lolcat / figlet

httpx / urllib3



---

⚡ Bonus Commands (optional aesthetic setup)

Make your terminal aesthetic AF:

pkg install figlet lolcat neofetch -y

Then run:

figlet st-find | lolcat


---

💬 Community

💀 Created by satan
📧 DM-friendly developer
🌐 Stay tuned for v3.0 (with real-time async scanning & web UI)


---

🧩 License

This project is released under the MIT License — feel free to modify, remix, and improve it!
Just give proper credit 🔥


---

🖤 Credits

> 💻 Dev: satan
🎨 Design & UX: also satan 😈
☕ Inspired by classic username checkers & Gen Z chaos energy



---

✅ **Copy & paste this entire block** into a file named `README.md`  
✅ Looks perfect on GitHub — colorful, clean, and super modern  
✅ You can replace `yourusername` in the clone link with your actual GitHub username  
