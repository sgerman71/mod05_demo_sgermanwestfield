from flask import Flask, g
from .app_factory import create_app

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment variable

# Register Blueprints
from app.blueprints.runners import runners

app.register_blueprint(runners)

from . import routes



