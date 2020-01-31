from flask_script import Manager
from app import app
from app.user.views import init_route

manager = Manager(app=app)
init_route(app)

if __name__ == '__main__':
    manager.run()
