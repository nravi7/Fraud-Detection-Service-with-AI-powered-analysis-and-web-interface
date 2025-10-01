#!/usr/bin/env bash
set -e
if [ -f ".venv/bin/activate" ]; then source .venv/bin/activate; fi
uvicorn app.main:app --host 0.0.0.0 --port 8000
