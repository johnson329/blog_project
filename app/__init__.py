from flask import Flask

from app.user import init_view


def create_app():
    app = Flask(__name__)
    init_view(app=app)
    return app


app = create_app()
