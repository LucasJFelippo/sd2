from flask import Flask, render_template, request
from blueprints.form import formbp

app = Flask(__name__, template_folder='templates')
app.register_blueprint(formbp)
app.secret_key = '-he9JTyn@dr5VFKM'


@app.route('/')
def index():
    return render_template('home.html')


def main():
    app.env = 'development'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()