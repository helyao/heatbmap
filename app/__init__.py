from flask import Flask
from flask.ext.pymongo import PyMongo
from config import config

def create_var(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint)

    mongo = PyMongo(app=app, config_prefix='MONGO')

    return app, mongo

