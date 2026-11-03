#!/bin/bash

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null && python --version 2>&1 | grep -qE "Python 3\."; then
    PYTHON_CMD=python
else
    echo "Error: Python 3 is not installed or not found in PATH"
    exit 1
fi

$PYTHON_CMD -m venv .venv
. .venv/bin/activate
$PYTHON_CMD -m pip install build
$PYTHON_CMD -m build --outdir dist ../
$PYTHON_CMD -m pip install dist/main_api_sdk-1.0.0-py3-none-any.whl --force-reinstall
