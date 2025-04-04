#!/bin/bash
cd /opt/render/project/src
export PYTHONPATH=/opt/render/project/src
gunicorn quantum_hermetic_gematria.app:app --bind 0.0.0.0:$PORT 