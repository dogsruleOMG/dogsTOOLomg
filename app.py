# This is a simple WSGI file that imports the Flask app from the quantum_hermetic_gematria directory

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add the current directory to the Python path
logger.debug(f"Current directory: {os.path.dirname(os.path.abspath(__file__))}")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Log Python path for debugging
logger.debug(f"Python path: {sys.path}")

try:
    # Import Flask app
    logger.debug("Importing app from quantum_hermetic_gematria.app")
    from quantum_hermetic_gematria.app import app
    logger.debug("Successfully imported app")
except Exception as e:
    logger.error(f"Error importing app: {str(e)}", exc_info=True)
    raise

# This allows Gunicorn to find the app variable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    logger.debug(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port) 