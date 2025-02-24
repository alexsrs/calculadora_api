from flask import Flask, request, jsonify

app = Flask(__name__)

#http://localhost:5000/somar?a=5&b=3
@app.route('/somar', methods=['GET'])
def somar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    soma = a + b
    return jsonify({'soma': soma})

#http://localhost:5000/subtrair?a=5&b=3
@app.route('/subtrair', methods=['GET'])
def subtrair():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    subtrair = a - b
    return jsonify({'subtrair': subtrair})

#http://localhost:5000/multiplicar?a=5&b=3
@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    multiplicar = a * b
    return jsonify({'multiplicar': multiplicar})

#http://localhost:5000/dividir?a=12&b=3
@app.route('/dividir', methods=['GET'])
def dividir():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    dividir = a / b
    return jsonify({'dividir': dividir})

if __name__ == '__main__':
    app.run(debug=True)