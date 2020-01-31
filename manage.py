from flask_script import Manager, Server
from app import app

manager = Manager(app=app)
manager.add_command("runserver", Server(use_debugger=True))


if __name__ == '__main__':
    manager.run()
