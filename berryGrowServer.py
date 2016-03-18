from flask import *

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    #user = {'nickname': 'Miguel'}  # fake user
    #return render_template('berrygrow.html', title='Home', user=user)
    with open('static/berrygrow.html', 'r') as content_file:
        content = content_file.read()


    return content

if __name__ == '__main__':
  app.run(
        port=int("5000")

  )
