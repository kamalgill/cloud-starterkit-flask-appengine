"""
Primary Flask app

"""
from flask import Flask
from flask_cors import CORS

from .api import api as api_blueprint
from .errors import add_error_handlers


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    add_error_handlers(app)
    return app


application = create_app()
