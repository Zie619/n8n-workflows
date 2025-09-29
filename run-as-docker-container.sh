#!/bin/bash
# N8N Workflows Documentation - Quick Docker Deployment

echo "🚀 Starting N8N Workflows Documentation with Docker"

# Use the new maintenance script for better management
./scripts/maintain.sh start

# Check if browser opening is supported
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  sleep 5 && open http://localhost:8000
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows
  sleep 5 && start http://localhost:8000
elif command -v xdg-open > /dev/null; then
  # Linux with desktop environment
  sleep 5 && xdg-open http://localhost:8000
else
  echo "✅ Application started successfully!"
  echo "🌐 Open http://localhost:8000 in your browser"
  echo "📊 API Documentation: http://localhost:8000/docs"
  echo ""
  echo "💡 Management commands:"
  echo "  View logs:    ./scripts/maintain.sh logs -f"
  echo "  Stop:         ./scripts/maintain.sh stop"
  echo "  Status:       ./scripts/maintain.sh status"
  echo "  Health:       ./scripts/maintain.sh health"
fi