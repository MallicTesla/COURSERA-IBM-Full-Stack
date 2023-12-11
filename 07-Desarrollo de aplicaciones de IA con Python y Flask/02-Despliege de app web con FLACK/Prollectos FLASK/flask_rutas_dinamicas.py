from flask import Flask, jsonify, request, render_template

# aca se crea una instansia de Flask y se le pasa el nombre de este archivo
app = Flask(__name__)

# para renderisar un html si o si tiene que estar en una carpeta templates
@app.route ("/MHTML")
def mhtml ():
    return render_template ("agrega_esto.html")

@app.route ("/metodos", methods = ["GET", "POST"])
def metodo ():
    if request.method == "GET":
        return jsonify (status = "OK", method = "GET"), 200

    if request.method == "POST":
        return jsonify (status = "OK", method = "POST"), 200


# ruta dinamica
# @app.route('/book/<isbn>')
# def get_author():
#     res = requests.get ("https://openlibrary.org/isbn/{escape(isbn)}.JSON")
#     if res.status_code == 200:
#         return {"Mensage": res.JSON()}

#     elif res.status_code == 404:
#             return {"Mensage": "No encontrado"}, 404

#     else:
#         return {"Mensage":"Error del servidor"}

if __name__ == '__main__':
    app.run(debug=True)