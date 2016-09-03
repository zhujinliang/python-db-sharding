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
    SQLALCHEMY_DATABASE_URI = 'mysql://dev_w:6nvjq0_HW@192.168.1.250:3307/dada'

    SQLALCHEMY_BINDS = {
        'coupon_db': 'mysql://dev_w:6nvjq0_HW@192.168.1.250:3307/coupon_service_db',
    }


config = Config()
