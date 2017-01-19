
class Config(object):
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017

    def init_app(self):
        pass

class DevelopmentConfig(Config):
    MONGO_BIN = r'd:\Program Files\MongoDB\Server\3.2\bin\mongod.exe'
    MONGO_DATA = r'd:\db1113'
    DEBUG = True
    USE_RELOADER = False    # use_reloader = False => not works ???

class ProductConfig(Config):
    MONGO_BIN = 'mongod'                    # when set environment variables
    MONGO_DATA = r'd:\MongoDB\database'

config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,

    'default': DevelopmentConfig
}