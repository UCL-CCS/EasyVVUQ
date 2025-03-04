#!/bin/bash

# Exit immediately if any command fails
set -e

# Define colors for output (native Bash ANSI escape codes)
GREEN="\e[32m"
BLUE="\e[34m"
YELLOW="\e[33m"
RED="\e[31m"
BOLD="\e[1m"
RESET="\e[0m"

# Function to print section headers
print_header() {
    echo -e "\n${BOLD}${BLUE}=============================================="
    echo -e " $1 "
    echo -e "==============================================${RESET}\n"
}

# Step 1: Define the directory for the virtual environment
VENV_DIR="./.venv"
REQUIREMENTS_FILE="requirements.txt"

print_header "Starting EasyVVUQ Installation"

# Step 2: Create a virtual environment in the EasyVVUQ directory
echo -e "${YELLOW}Creating a virtual environment in the EasyVVUQ directory...${RESET}"
python3 -m venv $VENV_DIR

# Step 3: Activate the virtual environment
echo -e "${YELLOW}Activating the virtual environment...${RESET}"
source $VENV_DIR/bin/activate

# Inform the user about activation for future use
echo -e "${GREEN}Note:${RESET} To use EasyVVUQ in this virtual environment later, run:"
echo -e "      ${BOLD}source $VENV_DIR/bin/activate${RESET}\n"

# Step 4: Upgrade essential tools
print_header "Upgrading Pip, Setuptools, and Wheel"
pip install --upgrade pip setuptools wheel

# Step 5: Install dependencies from requirements.txt
if [ -f "$REQUIREMENTS_FILE" ]; then
    print_header "Installing Dependencies from requirements.txt"
    pip install -r $REQUIREMENTS_FILE
else
    echo -e "${RED}Error:${RESET} requirements.txt not found in the EasyVVUQ directory!"
    exit 1
fi

# Step 6: Test the EasyVVUQ installation
print_header "Testing EasyVVUQ Installation"
python -c "import easyvvuq; print('EasyVVUQ version:', easyvvuq.__version__)"

print_header "Installation Completed Successfully!"
echo -e "${GREEN}Reminder:${RESET} Activate the virtual environment before using EasyVVUQ:"
echo -e "         ${BOLD}source $VENV_DIR/bin/activate${RESET}\n"

