from flask import Flask


app = Flask(__name__, static_url_path='')


@app.route('/')
def hello():
  return "<html><script type='text/javascript' src='ola.js'></script></html>"

if __name__ == '__main__':
  app.run( 
        host="localhost",
        port=int("5000")
  )