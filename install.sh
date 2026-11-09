#!/bin/bash

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null && python --version 2>&1 | grep -qE "Python 3\."; then
    PYTHON_CMD=python
else
    echo "Error: Python 3 is not installed or not found in PATH"
    exit 1
fi

USE_VENV=0

for arg in "$@"
do
    case $arg in
        --use-venv)
        USE_VENV=1
        shift
        ;;
    esac
done

if [ "$USE_VENV" -eq 1 ]; then
    $PYTHON_CMD -m venv .venv
    . .venv/bin/activate
fi

$PYTHON_CMD -m pip install build
$PYTHON_CMD -m build --outdir dist .
$PYTHON_CMD -m pip install dist/main_api_sdk-1.0.1-py3-none-any.whl --force-reinstall

if [ "$USE_VENV" -eq 1 ]; then
    deactivate
fi