#!/bin/bash

# Variables
SCRIPT_PATH="main.py"
ENV_PATH="venv"
CRON_SCHEDULE="*/5 * * * *"  # Every 5 min

# Create virtual environment
python3 -m venv $ENV_PATH

# Activate virtual environment and install dependencies
source $ENV_PATH/bin/activate
pip install -r requirements.txt  # If you have a requirements file

# Add cron job
(crontab -l ; echo "$CRON_SCHEDULE $ENV_PATH/bin/python $SCRIPT_PATH") | crontab -

# Ensure script is executable
chmod +x $SCRIPT_PATH

echo "Installation complete."
