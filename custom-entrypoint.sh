#!/bin/bash

# Wait for LocalStack to be ready
until curl -sSf http://localhost:4566/health | grep '"status": "running"' > /dev/null; do
  sleep 5
done

# Execute automate.sh script
./automate.sh

# Execute the command passed to the entrypoint
exec "$@"
