# WSGI entry point for Gunicorn

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add current directory to path
base_dir = os.path.dirname(os.path.abspath(__file__))
logger.debug(f"Current directory: {base_dir}")
sys.path.insert(0, base_dir)

# Explicitly import the Flask application
try:
    logger.debug("Attempting to import Flask app...")
    from quantum_hermetic_gematria.app import app as application
    
    # For Gunicorn compatibility
    app = application
    
    # Debug information
    logger.debug("Flask app successfully imported")
    logger.debug(f"Registered routes: {[rule.endpoint for rule in app.url_map.iter_rules()]}")
    logger.debug(f"Static folder: {app.static_folder}")
    logger.debug(f"Template folder: {app.template_folder}")
except Exception as e:
    logger.error(f"Failed to import Flask app: {str(e)}", exc_info=True)
    raise

# Direct execution (not via Gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    logger.debug(f"Starting Flask app on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True) 