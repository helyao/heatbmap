import pymongo
from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint)

    return app

def create_db(config_name):
    db = pymongo.MongoClient(host=config[config_name].MONGO_HOST,
                             port=config[config_name].MONGO_PORT)
    return db
