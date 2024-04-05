from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json


app = Flask(__name__)

# Banco em memória
banco = []

@app.route('/ping')
def ping():
    if ping:
        banco.append({
        "endereco":request.environ['REMOTE_ADDR'],
        "metodo": request.method,
        "hora":datetime.now()
        })
    
    return jsonify({"resposta": 'pong'})


@app.route('/echo', methods=['POST'])
def echo():
    texto = request.form.get('texto')
    if texto:
        banco.append({
        "endereco":request.environ['REMOTE_ADDR'],
        "metodo": request.method,
        "hora":datetime.now()
        })
        
    return jsonify({'dados': texto})
    
@app.route('/dash')
def dash():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('logs.html', itens=banco)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)



