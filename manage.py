from app import create_app, create_db
from flask_script import Manager, Shell

db = create_db('development')

app = create_app('development')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests."""
    pass

if __name__ == '__main__':
    manager.run()

