from flask_script import Manager, Server
from app import app

from flask_migrate import MigrateCommand

manager = Manager(app=app)
manager.add_command("runserver", Server(use_debugger=True))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
