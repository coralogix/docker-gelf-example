#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from flask import Flask

app = Flask(__name__)


@app.before_first_request
def setup_logging():
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(handler)


@app.route('/hello/<string:name>/')
def hello_world(name):
    response_text = 'Hello {0:s}!'.format(name)
    app.logger.info(response_text)
    return response_text


if __name__ == '__main__':
    app.run()
