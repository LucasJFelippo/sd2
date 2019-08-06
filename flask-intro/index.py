from flask import Flask
from funcionario import Funcionario

app = Flask(__name__)


def plus(a, b):
    return (a + b)


@app.route('/')
def indexinit():
    return "Pagina Inicial"

@app.route('/soma/<int:a>/<int:b>')
def testeinit(a, b):
    return "Teste de Soma: "+str(plus(a, b))

@app.route('/escrita/<string:a>')
def escritainit(a):
    return a

@app.route('/funcionario/<string:name>/<string:dep>')
def createfuncionario(name, dep):
    fun = Funcionario(name, dep)
    return fun.departamento


def main():
    app.env = 'development'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()