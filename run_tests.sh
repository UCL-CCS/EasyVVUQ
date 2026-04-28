#!/bin/bash
# Run tests securely by ensuring the virtual environment is loaded into PATH

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

python3 -m pytest --benchmark-skip tests/
