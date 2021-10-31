from flask import Flask
from datetime import datetime

def create_app(config_name):
    app = Flask(__name__)
    @app.route('/')
    def index():
        return 'welcome'

    return app