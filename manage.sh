#!/bin/bash

set -e  # Exit script on any error

SCRIPT_NAME="main.py"
ENV_NAME="venv"
CRON_SCHEDULE="*/5 * * * *"  # Every 5 minutes

# Function to install the script and setup cron job
install_script() {
    # Determine script directory
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_NAME"
    ENV_PATH="$SCRIPT_DIR/$ENV_NAME"

    # Create virtual environment if not exists
    if [ ! -d "$ENV_PATH" ]; then
        python3 -m venv "$ENV_PATH"
    fi

    # Activate virtual environment and install dependencies
    source "$ENV_PATH/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt"  # Assuming this file exists and contains dependencies

    # Add cron job if not already present
    if ! crontab -l | grep -q "$SCRIPT_PATH"; then
        (crontab -l 2>/dev/null; echo "$CRON_SCHEDULE $ENV_PATH/bin/python $SCRIPT_PATH") | crontab -
    fi

    # Ensure script is executable
    chmod +x "$SCRIPT_PATH"

    # Deactivate virtual environment
    deactivate

    echo "Installation complete."
}

# Function to start the cron job (no action needed, as cron will automatically start)

# Function to stop the cron job
stop_script() {
    # Remove cron job
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_NAME"
    (crontab -l | grep -v "$SCRIPT_PATH" | crontab -) || true  # Remove script from crontab, ignoring errors if not found
    echo "Cron job stopped."
}

# Handle command line arguments
case "$1" in
    install)
        install_script
        ;;
    start)
        echo "Nothing to do for starting the script (handled by cron)."
        ;;
    stop)
        stop_script
        ;;
    *)
        echo "Usage: $0 {install|start|stop}"
        exit 1
        ;;
esac

exit 0
