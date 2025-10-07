#!/usr/bin/env python3
# setup.py - Full Environment Setup for st-find

import os
import subprocess
import sys
import time

# Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

BANNER = r"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                              ┃
┃          🔧 st-find Full Setup Wizard        ┃
┃     ⚙️  Auto Installer for All Packages ⚙️     ┃
┃                                              ┃
┃            Created by: satan                 ┃
┃            Version: 2.0                      ┃
┃                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

def print_banner():
    try:
        subprocess.run(f"echo '{BANNER}' | lolcat", shell=True, check=False)
    except Exception:
        print(BANNER)

def run_command(cmd):
    """Ejecuta comandos del sistema mostrando salida"""
    try:
        print(f"{BLUE}[RUN]{RESET} {' '.join(cmd)}")
        subprocess.run(cmd, check=False)
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} {e}")

def main():
    os.system("clear")
    print_banner()

    print(f"{YELLOW}[?]{RESET} Do you want to install all required packages (15 total)?")
    choice = input(f"{BLUE}[?]{RESET} Type 'y' to continue or 'n' to cancel: ").strip().lower()

    if choice not in ["y", "yes"]:
        print(f"{RED}[x]{RESET} Installation cancelled.")
        sys.exit(0)

    print(f"\n{GREEN}[+]{RESET} Starting full installation process...\n")
    time.sleep(1)

    # --- APT/PKG packages ---
    apt_packages = [
        "python3", "python3-pip", "git", "curl",
        "lolcat", "figlet"
    ]

    print(f"{BLUE}[INFO]{RESET} Installing system dependencies via apt/pkg...\n")
    time.sleep(0.5)

    # Soporta apt o pkg (Termux)
    if os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
        manager = "pkg"
    else:
        manager = "apt"

    for pkg in apt_packages:
        run_command([manager, "install", pkg, "-y"])

    # --- PIP packages ---
    pip_packages = [
        "requests", "termcolor", "colorama", "beautifulsoup4", "rich",
        "lxml", "httpx", "urllib3", "fake_useragent", "pyfiglet", "tqdm"
    ]

    print(f"\n{BLUE}[INFO]{RESET} Installing Python dependencies via pip...\n")
    time.sleep(0.5)

    for pkg in pip_packages:
        run_command([sys.executable, "-m", "pip", "install", "-U", pkg])

    print(f"\n{GREEN}[✓]{RESET} All packages installed successfully!\n")
    print(f"{BLUE}[INFO]{RESET} You can now run {YELLOW}python3 st-find.py{RESET} 🚀")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[x]{RESET} Installation interrupted.")
