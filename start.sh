#!/bin/bash
# start.sh

echo "Iniciando bot com uvicorn..."
exec uvicorn bot:app --host 0.0.0.0 --port $PORT
