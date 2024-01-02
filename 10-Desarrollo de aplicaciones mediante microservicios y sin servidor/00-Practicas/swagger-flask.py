from flask import Flask, jsonify, request
import json

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask()

swaggerui_plano = get_swaggerui_blueprint (
    "/productos/doce",
    "http://{HOSTNAME}/swagger.json",
    config = {"app_name":"Microservicios"}
)

app.register_bluprint (swaggerui_plano)

@app.route ("swaggers.json")
def static_file ():
    return app.send_static_file ("swagger.json")