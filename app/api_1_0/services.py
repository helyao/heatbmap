from . import api

@api.route('/')
def index():
    return 'test'