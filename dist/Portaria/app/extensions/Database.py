from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def init_app(app):
    DB.init_app(app)