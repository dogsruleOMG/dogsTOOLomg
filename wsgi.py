import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add the application directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
logger.debug(f"Current directory: {current_dir}")

app_dir = os.path.join(current_dir, 'quantum_hermetic_gematria')
logger.debug(f"App directory: {app_dir}")

sys.path.insert(0, current_dir)
sys.path.insert(0, app_dir)

logger.debug(f"Python path: {sys.path}")

try:
    from quantum_hermetic_gematria.app import app
    logger.debug("Successfully imported app")
except Exception as e:
    logger.error(f"Failed to import app: {str(e)}")
    raise

if __name__ == "__main__":
    app.run() 