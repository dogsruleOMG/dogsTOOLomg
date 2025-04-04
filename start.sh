#!/bin/bash
cd /opt/render/project/src
export PYTHONPATH=/opt/render/project/src
gunicorn app:app --bind 0.0.0.0:$PORT 