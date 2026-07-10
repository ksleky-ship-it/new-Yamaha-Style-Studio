#!/bin/bash
set -e

echo "Yamaha StyleStudio Development Environment Setup"

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
    echo "Error: Python 3.10+ required"
    exit 1
fi

echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

echo "Installing dependencies..."
pip install -e ".[dev]"

echo "Setup complete!"
echo "Activate with: source venv/bin/activate"