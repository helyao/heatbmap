#__version__ = 1.0
#__description__ = 'Provide HeatBmap with data interface support'
from flask import Blueprint

api = Blueprint('api', __name__)

from . import errors, services