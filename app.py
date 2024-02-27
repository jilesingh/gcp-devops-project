from flask import Flask
app = Flask(__name__)

@app.route('/') # this is the base route
def hello_world():
    return "Hello, Simple Flask application"