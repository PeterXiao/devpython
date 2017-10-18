# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# filename: *.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()