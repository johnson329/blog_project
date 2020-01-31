def init_route(app):
    @app.route('/')
    def hello_world():
        return 'hello world!'
