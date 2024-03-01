#!/usr/bin/env python3

import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_pip():
    print("Attempting to install pip...")
    get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
    try:
        subprocess.check_call(["curl", get_pip_url, "-o", "get-pip.py"])
        subprocess.check_call([sys.executable, "get-pip.py"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pip: {e}")
        sys.exit(1)
    finally:
        try:
            subprocess.check_call(["rm", "get-pip.py"])
        except subprocess.CalledProcessError:
            pass  # If removing get-pip.py fails, it's not a fatal error

def check_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    if not check_pip():
        print("pip is not installed.")
        install_pip()

    print("Installing Ansible...")
    try:
        install_package("ansible")
        print("Ansible installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Ansible: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
