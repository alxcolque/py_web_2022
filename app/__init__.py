from flask import Flask
app = Flask(__name__) 
@app.route('/')
def index():
    return '<h1>Hola {}!<h1>'.format(__name__)
    #return "hello world"
 