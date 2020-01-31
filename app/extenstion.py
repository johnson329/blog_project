from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


models = SQLAlchemy()
migrate=Migrate()
def init_ext(app):
    models.init_app(app=app)
    migrate.init_app(app=app,db=models)


