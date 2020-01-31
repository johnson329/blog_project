from flask import Flask
from flask_script import Manager
from app.user.views import init_route

app = Flask(__name__)
manager = Manager(app=app)
init_route(app)

if __name__ == '__main__':
    manager.run()
