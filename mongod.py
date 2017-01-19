# -*- coding:utf-8 -*-
import os
import time
import subprocess
from config import config

class MongodManager(object):

    class _mongod(object):

        def __init__(self, mode):
            self.id = id(self)
            # start mongod in 127.0.0.1:27017
            if self._isMongodRunning():
                print('Service mongod existed...')
            else:
                self._mongodStart(mode)

        def _isMongodRunning(self):
            result = subprocess.Popen('tasklist | find "mongod.exe"', shell=True, stdout=subprocess.PIPE).communicate()[0]
            print(result.decode('utf-8'))
            return True if len(result.decode('utf-8')) > 0 else False

        def _mongodStart(self, mode):
            cmd = os.path.join(config[mode].MONGO_BIN) + ' --dbpath ' + config[mode].MONGO_DATA
            print('Start mongod service...')
            print(cmd)
            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(5)
            print('Service mongod running.')

        def _mongodKill(self):
            return os.system(r'taskkill /F /IM "mongod.exe"')

    _mongodcheck = None

    def __init__(self, mode):
        if MongodManager._mongodcheck is None:
            MongodManager._mongodcheck = MongodManager._mongod(mode)

    # use MongoManager.key can access MongoManager._mongod.key directly
    def __getattr__(self, item):
        return getattr(self._mongodcheck, item)

    def killMongodService(self):
        if MongodManager._mongodcheck is not None:
            self._mongodcheck._mongodKill()
            return True
        return False

if __name__ == '__main__':
    mongod1 = MongodManager('development')
    mongod2 = MongodManager('development')
    print(mongod1.id)
    print(mongod2.id)
    mongod2.killMongodService()