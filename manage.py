# -*- coding:utf-8 -*-
from app import create_var
from mongod import MongodManager
from flask_script import Manager, Shell

RUN_MODE = 'development'

app, mongo = create_var(RUN_MODE)
manager = Manager(app)

def make_shell_context():
    return dict(app=app, mongo=mongo)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests."""
    pass

@manager.command
def testmongod():
    mongochk = MongodManager(RUN_MODE)
    mongochk.killMongodService()

if __name__ == '__main__':

    manager.run()

