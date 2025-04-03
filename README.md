# Quantum Hermetic Gematria App

A web application for quantum-hermetic gematria analysis with Egyptian technology mappings and modern equivalents.

## Features
- Single phrase quantum analysis
- Two-phrase comparison
- Egyptian technology resonance mapping
- Modern equivalent detection
- History tracking with session management

## Deployment Instructions

### Quick Deploy to Render
1. Fork this repository to your GitHub account
2. Go to [render.com](https://render.com) and create an account
3. Click "New +" and select "Web Service"
4. Connect your GitHub account and select this repository
5. Use these settings:
   - Name: quantum-hermetic-gematria
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn quantum_hermetic_gematria.app:app`
6. Click "Create Web Service"

The app will be deployed and available at a URL like: `https://quantum-hermetic-gematria.onrender.com`

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python quantum_hermetic_gematria/app.py
```

## Usage
1. Access the web interface
2. Enter a phrase to analyze its quantum resonance
3. Compare two phrases to see their compatibility
4. View Egyptian technology alignments and modern equivalents
5. Track your analysis history 