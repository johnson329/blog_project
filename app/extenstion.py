from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

models = SQLAlchemy()
migrate=Migrate()
bootstrap=Bootstrap()
def init_ext(app):
    models.init_app(app=app)
    migrate.init_app(app=app,db=models)
    bootstrap.init_app(app=app)


