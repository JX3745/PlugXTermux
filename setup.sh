#!/bin/bash

echo -e "\033[1;33mStarting PlugXTermux setup...\033[0m"

# Updating and upgrading Termux
pkg update -y && pkg upgrade -y || { echo "Failed to update Termux. Exiting."; exit 1; }

# Installing dependencies
pkg install python curl flask -y || { echo "Failed to install dependencies. Exiting."; exit 1; }

# Installing Python packages
pip install --no-cache-dir requests cryptography python-dotenv colorama || { echo "Failed to install Python packages. Exiting."; exit 1; }

echo -e "\033[1;32mSetup complete! Run 'python plugxtermux.py' to start.\033[0m"
