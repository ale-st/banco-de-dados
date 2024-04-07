'''
ALUNOS:
JOAO PAULO FRAGA SANTOS
CARLOS ALEXANDRE DA SILVA SANTOS
BRUNO EDUARDO DO NASCIMENTO GOMES
'''

import json
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def conectar_bd():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='professor',
            password='professor',
            host='aplicacaofinal.cnpire5o3emt.us-east-1.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

#função para consultar dados na tabela funcionario
@app.route('/consultar_funcionario')
def consultar_funcionario():
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM locadora.funcionario")
            resultados = cursor.fetchall()
            dados_json = []
            for linha in resultados:
                dados_json.append({
                    'CPF': linha[0],
                    'cargo': linha[1],
                    'email': linha[2],
                    'nomecompleto': linha[3]
                })
            conn.close()
            return jsonify(dados_json)
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao consultar o banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para excluir dados na tabela funcionario usando o CPF
@app.route('/excluir_funcionario/<string:cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM locadora.funcionario WHERE CPF = %s", (cpf,))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'Funcionário excluído com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao excluir funcionário do banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para inserir dados na tabela funcionario
@app.route('/inserir_funcionario', methods=['POST'])
def inserir_funcionario():
    conn = conectar_bd()
    if conn is not None:
        try:
            novo_funcionario = request.json
            cpf = novo_funcionario['CPF']
            cargo = novo_funcionario['cargo']
            email = novo_funcionario['email']
            nomecompleto = novo_funcionario['nomecompleto']

            cursor = conn.cursor()
            cursor.execute("INSERT INTO locadora.funcionario (CPF, cargo, email, nomecompleto) VALUES (%s, %s, %s, %s)",
                           (cpf, cargo, email, nomecompleto))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'Funcionário inserido com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao inserir funcionário no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para atualizar dados na tabela funcionario usando o CPF como base
@app.route('/atualizar_funcionario/<string:cpf>', methods=['PUT'])
def atualizar_funcionario(cpf):
    conn = conectar_bd()
    if conn is not None:
        try:
            novos_dados = request.json
            novo_cargo = novos_dados['cargo']
            novo_email = novos_dados['email']
            novo_nomecompleto = novos_dados['nomecompleto']

            cursor = conn.cursor()
            cursor.execute("UPDATE locadora.funcionario SET cargo = %s, email = %s, nomecompleto = %s WHERE CPF = %s",
                           (novo_cargo, novo_email, novo_nomecompleto, cpf))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'Dados do funcionário atualizados com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao atualizar dados do funcionário no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para consultar dados na tabela manutenção
@app.route('/consultar_manutencao')
def consultar_manutencao():
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM locadora.manutencao")
            resultados = cursor.fetchall()
            dados_json = []
            for linha in resultados:
                dados_json.append({
                    'id_manutencao': linha[0],
                    'data': linha[1],
                    'preco': linha[2],
                    'motivo': linha[3]
                })
            conn.close()
            return jsonify(dados_json)
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao consultar o banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para excluir dados na tabela manutenção usando o id_manutencao para buscar na tabela
@app.route('/excluir_manutencao/<int:id_manutencao>', methods=['DELETE'])
def excluir_manutencao(id_manutencao):
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM locadora.manutencao WHERE id_manutencao = %s", (id_manutencao,))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'manutencao excluído com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao excluir manutencao do banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para inserir dados na tabela manutenção
@app.route('/inserir_manutencao', methods=['POST'])
def inserir_manutencao():
    conn = conectar_bd()
    if conn is not None:
        try:
            nova_manutencao = request.json
            id_manutencao = nova_manutencao['id_manutencao']
            data = nova_manutencao['data']
            preco = nova_manutencao['preco']
            motivo = nova_manutencao['motivo']

            cursor = conn.cursor()
            cursor.execute("INSERT INTO locadora.manutencao (id_manutencao, data, preco, motivo) VALUES (%s, %s, %s, %s)",
                           (id_manutencao, data, preco, motivo))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'manutencao inserido com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao inserir manutencao no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para atualizar dados na tabela manutenção usando como base o id_manutenção
@app.route('/atualizar_manutencao/<int:id_manutencao>', methods=['PUT'])
def atualizar_manutencao(id_manutencao):
    conn = conectar_bd()
    if conn is not None:
        try:
            novos_dados = request.json
            nova_data = novos_dados['data']
            novo_preco = novos_dados['preco']
            novo_motivo = novos_dados['motivo']

            cursor = conn.cursor()
            cursor.execute("UPDATE locadora.manutencao SET data = %s, preco = %s, motivo = %s WHERE id_manutencao = %s",
                           (nova_data, novo_preco, novo_motivo, id_manutencao))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'Dados de manutencao atualizados com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao atualizar dados da manutencao no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para consultar dados na tabela entra_manutenção
@app.route('/consultar_entra_manutencao')
def consultar_entra_manutencao():
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM locadora.entra_manutencao")
            resultados = cursor.fetchall()
            dados_json = []
            for linha in resultados:
                dados_json.append({
                    'funcionario_cpf': linha[0],
                    'manutencao_id_manutencao': linha[1]
                })
            conn.close()
            return jsonify(dados_json)
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao consultar o banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para excluir dados da tabela entra_manutenção usando como base o id_manutencao
@app.route('/excluir_entra_manutencao/<int:id_manutencao>', methods=['DELETE'])
def excluir_entra_manutencao(id_manutencao):
    conn = conectar_bd()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM locadora.entra_manutencao WHERE manutencao_id_manutencao = %s", (id_manutencao,))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'entra_manutencao excluído com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao excluir entra_manutencao do banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para inserir dados na tabela entra_manutenção
@app.route('/inserir_entra_manutencao', methods=['POST'])
def inserir_entra_manutencao():
    conn = conectar_bd()
    if conn is not None:
        try:
            # Obtendo os dados do novo funcionário do corpo da requisição
            nova_manutencao = request.json
            funcionario_cpf = nova_manutencao['funcionario_cpf']
            manutencao_id_manutencao = nova_manutencao['manutencao_id_manutencao']

            cursor = conn.cursor()
            cursor.execute("INSERT INTO locadora.entra_manutencao (funcionario_cpf, manutencao_id_manutencao) VALUES (%s, %s)",
                           (funcionario_cpf, manutencao_id_manutencao))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'entra_manutencao inserido com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao inserir entra_manutencao no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#função para atualizar a tabela entra_manutencao
@app.route('/atualizar_entra_manutencao/<int:manutencao_id_manutencao>', methods=['PUT'])
def atualizar_entra_manutencao(manutencao_id_manutencao):
    conn = conectar_bd()
    if conn is not None:
        try:
            # Obtendo os novos dados do funcionário do corpo da requisição
            novos_dados = request.json
            novo_cpf = novos_dados['funcionario_cpf']
            #novo_id_manutencao = novos_dados['id_manutencao']

            cursor = conn.cursor()
            cursor.execute("UPDATE locadora.entra_manutencao SET funcionario_cpf = %s WHERE manutencao_id_manutencao = %s;",
                           (novo_cpf, manutencao_id_manutencao))
            conn.commit()
            conn.close()
            return jsonify({'mensagem': 'Dados de entra_manutencao atualizados com sucesso'})
        except psycopg2.Error as e:
            print("Erro ao executar consulta SQL:", e)
            return jsonify({'erro': 'Erro ao atualizar dados de entra_manutencao no banco de dados'})
    else:
        return jsonify({'erro': 'Erro ao conectar ao banco de dados'})

#essa linha abaixo precisa para rodar o Flask
if __name__ == '__main__':
    app.run(debug=True)
