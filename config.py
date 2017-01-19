
class Config(object):

    def init_app(self):
        pass

class DevelopmentConfig(Config):
    MONGO_BIN = r'd:\Program Files\MongoDB\Server\3.2\bin\mongod.exe'
    MONGO_DATA = r'd:\db1113'
    # DBORIGIN_* -> production db, store origin data from collector
    DBORIGIN_HOST = '127.0.0.1'
    DBORIGIN_PORT = 27017
    DBORIGIN_DBNAME = 'envdb'
    # DBTEMP_* -> heatbmap task array data
    DBTEMP_HOST = '127.0.0.1'
    DBTEMP_PORT = 27017
    DBTEMP_DBNAME = 'temp'
    # Configure for flask
    DEBUG = True
    # USE_RELOADER = False    # use_reloader = False => not works ???

class ProductConfig(Config):
    MONGO_BIN = 'mongod'                    # when set environment variables
    MONGO_DATA = r'd:\MongoDB\database'

config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,

    'default': DevelopmentConfig
}