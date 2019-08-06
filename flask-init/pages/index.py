from flask import Flask, render_template, request, session
import sys

sys.path.append('../database/')
import piton.test as test


app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    test.world()
    print(sys.path)
    return render_template('home.html')


def main():
    app.env = 'development'
    app.secret_key = 'A chave secreta e: batata'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()