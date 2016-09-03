# -*- coding -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.configs import config


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']
    return app

app = create_app(config)


db = SQLAlchemy(app)
