import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('Calculadora.html')


@app.route('/teste', methods=['POST', 'GET'])
def teste():
    return render_template('Calculadora.html')


@app.route('/calculaform', methods=['POST', 'GET'])
def Calc():
    valor1 = request.form['num1']
    valor2 = request.form['num2']
    op = request.form['operacao']

    v1 = int(valor1)
    v2 = int(valor2)

    if(op == 'soma'):
        resultado = v1 + v2
    elif(op == 'subtração'):
        resultado = v1 - v2
    elif(op == 'divisão'):
        resultado = v1 / v2
    elif(op == 'multiplicação'):
        resultado = v1 * v2

    return str(resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
