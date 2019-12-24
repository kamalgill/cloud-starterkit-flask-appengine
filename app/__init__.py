"""
Primary Flask app

"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    return app


application = create_app()
