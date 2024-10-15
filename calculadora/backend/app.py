from flask import Flask
from flask_cors import CORS
import math as mt
from flask import jsonify

app=Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0, numero2=0):
    resultado = numero1 + numero2
    data = {
        "resultado": resultado,
        "operacion": "Suma"
    }
    return jsonify(data)

@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")

def resta(numero1=0, numero2=0):
    resultado = numero1 - numero2
    data = {
        "resultado": resultado,
        "operacion": "Resta"
    }
    return jsonify(data)

@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicacion(numero1=0, numero2=0):
    resultado = numero1 * numero2
    data = {
        "resultado": resultado,
        "operacion": "Multiplicación"
    }
    return jsonify(data)

@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
def division(numero1=0, numero2=0):
    if numero2 == 0:
        return jsonify({"error": "No se puede dividir por cero."}), 400
    resultado = numero1 / numero2
    data = {
        "resultado": resultado,
        "operacion": "División"
    }
    return jsonify(data)

@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0, numero2=0):
    resultado=numero1**numero2
    data = {
        "resultado": resultado,
        "operacion": "Potenciación"
    }
    return jsonify(data)

@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado = mt.sin(numero1)
    data = {
        "resultado": resultado,
        "operacion": "Seno"
    }
    return jsonify(data)

@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado = mt.cos(numero1)
    data = {
        "resultado": resultado,
        "operacion": "Coseno"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
