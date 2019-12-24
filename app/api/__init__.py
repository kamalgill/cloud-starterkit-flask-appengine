"""
Blueprint for API endpoints

"""
from flask import Blueprint


api = Blueprint('api', __name__)


from . import hello
