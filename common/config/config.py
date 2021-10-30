import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)

class DevelopmentConfig():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("gogolook.db")

class TestingConfig():
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_ECHO = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}