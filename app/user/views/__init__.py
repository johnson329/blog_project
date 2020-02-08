from .views import user_bp
from .m2m import m2m_bp
from .github_login import github_bp



def init_view(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(m2m_bp)
    app.register_blueprint(github_bp)
