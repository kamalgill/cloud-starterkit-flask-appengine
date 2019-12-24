"""
Hello API route handlers

"""
from flask import jsonify

from . import api


@api.route('/hello/<name>')
def hellow(name):
    return jsonify(dict(hello=name))
