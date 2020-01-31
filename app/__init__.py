from flask import Flask

from app.extenstion import init_ext
from app.user import init_view


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # 执行先后顺序无关
    init_view(app=app)
    init_ext(app=app)
    return app


app = create_app()
