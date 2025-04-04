# This is a simple WSGI file that imports the Flask app from the quantum_hermetic_gematria directory

# Import Flask app
from quantum_hermetic_gematria.app import app

# This allows Gunicorn to find the app variable
if __name__ == "__main__":
    app.run() 