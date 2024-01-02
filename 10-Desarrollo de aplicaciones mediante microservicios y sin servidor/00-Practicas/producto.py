from flask import Flask, jsonify, request
import json

app = Flask(__name__)

producto = [
    {"ide":123, "name":"primero", "presio":15.5},
    {"ide":556, "name":"segundo", "presio":19.5}
]

@app.route ("/productos", methods = ["GET"])
def productos ():
    return jsonify (producto)