#!/bin/bash
echo "=== Health Check ==="
RESPONSE=$(curl -s http://localhost:5000/api/health)
echo "Response: $RESPONSE"
if echo "$RESPONSE" | grep -q "healthy"; then
    echo "✅ API is healthy"
else
    echo "❌ API is down!"
fi