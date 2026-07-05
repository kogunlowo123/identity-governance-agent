#!/bin/bash
set -euo pipefail
echo "Setting up Identity Governance Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
