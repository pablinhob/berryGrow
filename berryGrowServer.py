#!/usr/bin/python


from flask import *
import pprint
import json
import os

pathMachinesConf = os.getcwd()+'/conf/machinesConf.json'
pathMachinesStatus = os.getcwd()+'/conf/machinesStatus.json'

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    with open('static/berrygrow.html', 'r') as content_file:
        content = content_file.read()
    return content

@app.route('/getStatus')
def getStatus():
    return Response(open( pathMachinesStatus ).read(), mimetype='text/json')

@app.route('/getConf')
def getConf():
    return Response(open( pathMachinesConf ).read(), mimetype='text/json')

@app.route('/setStatus', methods = ['POST'])
def setStatus():
    ret = 'true'
    try:
        jsonObj = json.load( request.form['statusData'] )
    except ValueError, e:
        ret =  '"Invalid JSON"'
    else:
        with open( pathMachinesStatus , 'w') as outfile:
            json.dump( jsonObj, outfile )

    return ret

@app.route('/setConf', methods = ['POST'])
def setConf():
    ret = 'true'

    try:
        jsonObj = json.load( request.form['confData'] )
    except ValueError, e:
        ret =  '"Invalid JSON"'
    else:
        with open( pathMachinesConf , 'w') as outfile:
            json.dump( jsonObj, outfile )

    return Response(response= '{ "response": ' + ret + ' }',
                        status=200,
                        mimetype="application/json")


if __name__ == '__main__':
    #app.debug = True
    app.run( host="0.0.0.0", port=5000 )
