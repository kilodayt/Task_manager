#!/bin/bash
# wait-for-it.sh - wait for a given service to be available
host="$1"
shift
port="$1"
shift
timeout="$1"
shift
# Wait until the PostgreSQL is available
until nc -z -v -w30 $host $port; do
  echo "Waiting for database at $host:$port..."
  sleep 1
done
# Once DB is available, run the migration and start server
echo "Database is up!"
exec "$@"
