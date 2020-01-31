from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.user import init_view
from app.user.models import init_model

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    #执行先后顺序无关
    init_view(app=app)
    init_model(app=app)
    return app


app = create_app()
