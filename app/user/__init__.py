from .views import user_bp


def init_view(app):
    app.register_blueprint(user_bp)
