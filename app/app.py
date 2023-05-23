import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from db_handler import DB

db = DB(os.path.dirname(os.path.realpath(__file__)))
db.init_db()

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    cors = CORS(app, resources={'/*': {"origins": "*"}})
    return app

app = create_app()


@app.route('/', methods=['GET'])
def index(): 
    if  not request.args:
        return render_template('index.html', error='')
    
    error = ''
    prod = request.args['prod']

    if not prod:
        error = 'Product name is required.'
    else:
        prod = db.get(prod)

        if prod is None:
            error = 'Product does not exist.'

    if not error:
        flash(prod)
        return redirect(url_for('index'))

        
    return render_template('index.html', error=error)


if __name__ == "__main__":
    # Production
    print("starting the server ....")
    http_server = WSGIServer(('', 5000), app)
    print("Server is Up, enjoy :)")
    http_server.serve_forever()
