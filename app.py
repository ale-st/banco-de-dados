import json
from flask import Flask, jsonify, request
a = open("C://Users//jpfs0//OneDrive//Área de Trabalho//mochila//testeBanco.txt", "w")
app = Flask(__name__)
#comentario
usuario = [
    {
        'CPF': '123.456.789.12',
        'nome': 'joão da silva',
        'Data de nascimento': '12/12/1992' 
    },
    {
        'CPF': '392.285.182.15',
        'nome': 'pedro',
        'Data de nascimento': '19/01/2001' 
    },
    {
        'CPF': '869.956.492.29',
        'nome': 'paulo',
        'Data de nascimento': '03/05/1997' 
    }
]
#consultar todos
@app.route('/usuario', methods=['GET'])
def pegar_usuario():
    return jsonify(usuario)

@app.route('/usuario', methods=['POST'])
def incluir():
    novoUsuario = request.get_json()
    usuario.append(novoUsuario)
    #a.write(novoUsuario)
    a.write(json.dumps(novoUsuario))
    a.write('\n')
    return jsonify(usuario)

app.run(port=5000,host='127.0.0.1',debug=True)
a.close()
