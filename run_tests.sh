#!/bin/bash
# Run tests using the virtual environment if available, otherwise use system python

if [ -f ".venv/bin/python" ]; then
    PYTHON_BIN=".venv/bin/python"
else
    PYTHON_BIN="python3"
fi

$PYTHON_BIN -m pytest --benchmark-skip tests/
