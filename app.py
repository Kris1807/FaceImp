"""Deployment entrypoint for the web demo.

This keeps the main FastAPI application in web_app.py so local development and
hosted deployments can both import the same app object.
"""

from web_app import app
