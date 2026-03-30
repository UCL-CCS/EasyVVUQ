#!/bin/bash
# Run tests using the virtual environment if available, otherwise use system python

if [ -f ".venv/bin/python" ]; then
    .venv/bin/python -m pytest tests/
else
    python3 -m pytest tests/
fi

