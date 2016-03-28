#!/usr/bin/python

from flask import *
import pprint


app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    with open('static/berrygrow.html', 'r') as content_file:
        content = content_file.read()
    return content
@app.route('/read')
def read():
    return "READDDDDD"


if __name__ == '__main__':

  app.run( host="0.0.0.0", port=5000 )









 # d = shelve.open('persist.pid')
 # d['berryGrow'] = machines
