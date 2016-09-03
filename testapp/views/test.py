# -*- coding:utf-8 -*-

from core import app

@app.route('/')
def hello_world():
    return 'Hello World!'
