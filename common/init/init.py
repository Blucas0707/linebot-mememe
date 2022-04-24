from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    @app.route('/')
    def index():
        return 'welcome'

    return app
