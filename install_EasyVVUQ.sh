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
TOML_FILE="pyproject.toml"

print_header "Starting EasyVVUQ Installation"

# Step 2: Create a virtual environment in the EasyVVUQ directory
if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Virtual environment already exists. Removing and recreating...${RESET}"
    rm -rf $VENV_DIR
fi

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

# Install build tools for modern Python packaging
echo -e "${YELLOW}Installing build dependencies...${RESET}"
pip install build

# Step 5: Install dependencies from requirements.txt
if [ -f "$REQUIREMENTS_FILE" ]; then
    print_header "Installing Dependencies from requirements.txt"
    pip install -r $REQUIREMENTS_FILE
else
    echo -e "${RED}Error:${RESET} requirements.txt not found in the EasyVVUQ directory!"
    exit 1
fi

# Step 6: Install local easyvvuq
if [ -f "$TOML_FILE" ]; then
    print_header "Installing local easyvvuq (from src) based on $TOML_FILE"
    pip install -e .
else
    echo -e "${RED}Error:${RESET} $TOML_FILE not found in the EasyVVUQ directory!"
    exit 1
fi

# Step 7: Test the EasyVVUQ installation
print_header "Testing EasyVVUQ Installation"

# Test that the import works
echo -e "${YELLOW}Testing import...${RESET}"
python -c "import easyvvuq; print('✓ Import successful')" || {
    echo -e "${RED}Error:${RESET} Failed to import easyvvuq"
    exit 1
}

# Test version access
echo -e "${YELLOW}Checking version...${RESET}"
python -c "import easyvvuq; print('EasyVVUQ version:', easyvvuq.__version__)" || {
    echo -e "${YELLOW}Warning:${RESET} Could not access version through __version__, trying alternative..."
    python -c "import easyvvuq; print('EasyVVUQ installed successfully')"
}

# Test a basic functionality
echo -e "${YELLOW}Testing basic functionality...${RESET}"
python -c "
import easyvvuq as uq
import tempfile
import os

# Test creating a campaign
with tempfile.TemporaryDirectory() as tmpdir:
    campaign = uq.Campaign(name='test', work_dir=tmpdir)
    print('✓ Campaign creation successful')
    print('✓ Basic functionality test passed')
"

print_header "Installation Completed Successfully!"
echo -e "${GREEN}Reminder:${RESET} Activate the virtual environment before using EasyVVUQ:"
echo -e "         ${BOLD}source $VENV_DIR/bin/activate${RESET}\n"

