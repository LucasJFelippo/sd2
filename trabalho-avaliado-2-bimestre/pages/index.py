from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request
import sys

sys.path.append('../database/')
from model.ideia import Ideia
from model.usuario import Usuario
from dao.ideiadao import IdeiaDao
from dao.usuariodao import UsuarioDao


app = Flask(__name__, template_folder='template')
app.secret_key = 'secretkey'


@app.before_request
def verify():
    if 'login' not in session and request.endpoint != 'index' and request.endpoint != 'login':
        return redirect(url_for('index'))

@app.route('/')
def index():
    if 'login' in session:
        return render_template('select.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if verifylogin(request.form['username'], request.form['password']):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('cod', None)
    session.pop('nome', None)
    session.pop('login', None)
    return redirect(url_for('index'))

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idao = IdeiaDao()
        user = Usuario(cod = session["cod"])
        ideia = Ideia(titulo = request.form['titulo'], descricao = request.form['descricao'], usuario = user)
        idao.salvar(ideia)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/listar')
def listar():
    idao = IdeiaDao()
    array = idao.listar(100, 0)
    return render_template('listar.html', array=array)

@app.route('/descricao/<int:cod>')
def descricao(cod):
    idao = IdeiaDao()
    ideia = idao.buscar(cod)
    return render_template('detalhe.html', ideia=ideia)

@app.route('/deletar', methods=['POST'])
def deletar():
    idao = IdeiaDao()
    ideia = Ideia(cod = request.form['cod'])
    idao.excluir(ideia)
    return redirect(url_for('listar'))

@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
    idao = IdeiaDao()
    ideia = idao.buscar(request.form['cod'])
    return render_template('alterar.html', ideia=ideia)

@app.route('/alt', methods=['GET', 'POST'])
def alt():
    if request.method == 'POST':
        idao = IdeiaDao()
        ideia = idao.buscar(request.form['cod'])
        ideia.titulo = request.form['titulo']
        ideia.descricao = request.form['descricao']
        user = Usuario(cod = request.form['usuario'])
        ideia.usuario = user
        idao.salvar(ideia)
        return redirect(url_for('listar'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')


def verifylogin(username, password):
    usrdao = UsuarioDao()
    usr = Usuario(login = username, senha = password)
    verify = usrdao.buscar(usr)
    if verify:
        session['cod'] = verify.cod
        session['nome'] = verify.nome
        session['login'] = verify.login
        return True
    else:
        return False


def main():
    app.env = 'development'
    app.secret_key = 'A chave secreta e: batata'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()