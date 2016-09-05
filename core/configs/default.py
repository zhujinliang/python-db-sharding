# -*- encoding: utf8 -*-

import os

PROJECT_PATH = os.path.abspath(
                    os.path.join(
                        os.path.abspath(os.path.dirname(__file__)),
                        os.pardir, os.pardir))


class Config(object):

    TEMPLATE_FOLDER = PROJECT_PATH + 'testapp/templates'
    STATIC_FOLDER = PROJECT_PATH + 'testapp/static'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://test:test@192.168.1.250:3306/test'

    SQLALCHEMY_BINDS = {
        'coupon_db': 'mysql://test:test@192.168.1.250:3306/test',
    }

    SHARDING_NUM = 10


config = Config()
