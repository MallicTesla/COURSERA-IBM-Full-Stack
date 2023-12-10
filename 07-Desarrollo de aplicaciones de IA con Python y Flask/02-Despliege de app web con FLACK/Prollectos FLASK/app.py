from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # return '<b> Funciono mi primer "projecto" de Flask </b>'

    # asi se puede devolver un objeto json
    # return {"mensage": '<b> Funciono mi primer "projecto" de Flask </b>'}
    return jsonify (mensage = '<b> Funciono mi primer "projecto" de Flask </b>')


if __name__ == '__main__':
    app.run(debug=True)
