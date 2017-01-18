
class Config(object):
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017

    def init_app(self):
        pass

class DevelopmentConfig(Config):
    MONGO_HOME = r'd:\Program Files\MongoDB\Server\3.2\bin'
    MONGO_DATA = r'd:\db1113'
    DEBUG = True
    USE_RELOADER = False

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}