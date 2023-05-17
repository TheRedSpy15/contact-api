from app import app

if __name__ == "__main__":
    app.run()

# Add the following lines at the end
import os
from werkzeug.middleware.proxy_fix import ProxyFix

# Wrap the Flask app with ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

# Create the Gunicorn entry point
def create_app(environ, start_response):
    return app(environ, start_response)
