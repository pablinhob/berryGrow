#!/usr/bin/python

from flask import *
import pprint


pathMachinesConf = os.getcwd()+'conf/machinesConf.json')
pathMachinesStatus = os.getcwd()+'conf/machinesStatus.json')

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    with open('static/berrygrow.html', 'r') as content_file:
        content = content_file.read()
    return content

@app.route('/getStatus')
def getStatus():
    return Response(response= json.loads( open( pathMachinesStatus ).read() ),
                    status=200,
                    mimetype="application/json")

@app.route('/getConf')
def getConf():
    return Response(response= json.loads( open( pathMachinesConf ).read() ),
                    status=200,
                    mimetype="application/json")

@app.route('/setStatus', methods = ['POST'])
def setStatus():
    request.form['statusData']:
    return True

@app.route('/setConf', methods = ['POST'])
def setConf():
    request.form['confData']:
    return True


if __name__ == '__main__':
  app.run( host="0.0.0.0", port=5000 )
