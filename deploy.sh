#!/bin/bash
echo "=== Deploying Proptech API ==="
echo "1. Pulling latest code..."
git pull
echo "2. Installing dependencies..."
pip3 install -r requirements.txt
echo "3. Restarting service..."
pkill -f "python3 app.py" || true
python3 app.py &
echo "=== Deployment complete ==="