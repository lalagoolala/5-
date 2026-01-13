"""
WSGI entry point for production deployment.
This file is used for Vercel, Heroku, Railway, and other platforms.
"""

import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

# For Vercel
app = app

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
