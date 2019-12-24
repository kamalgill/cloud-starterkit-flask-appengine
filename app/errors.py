"""
API error handlers

"""
from flask import jsonify


def add_error_handlers(app):
    @app.errorhandler(404)
    def not_found(err):
        error_response = dict(error=err.name, status=err.code)
        response = jsonify(error_response)
        response.status_code = 404
        return response
