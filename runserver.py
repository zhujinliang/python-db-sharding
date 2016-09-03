# -*- encoding: utf8 -*-

from core import app
import testapp.views

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=app.debug)
