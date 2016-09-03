# -*- coding: utf-8 -*-

from .default import Config


class DevelopConfig(Config):

    DEBUG = True


config = DevelopConfig()
