from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "App Barbearia"

@app.route('/novofuncionario')
def adicionar_funcionario():
    return "funcionário adicionado"


@app.route('/novocliente')
def adicionar_cliente():
    return "cliente adicionado"

@app.route('/novoservico')
def adicionar_agendamento():
    return "agendamento adicionado"

@app.route('/novologin')
def adicionar_login():
    return "login adicionado"

@app.route('/novologout')
def adicionar_logout():
    return "logout adicionado"





app.run(debug=True)