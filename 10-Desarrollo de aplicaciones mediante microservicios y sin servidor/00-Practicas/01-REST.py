from flask import Flask

app = Flask(__name__)

@app.route ("/")
def funciona ():
    return "<h1> Funciono </h1>"