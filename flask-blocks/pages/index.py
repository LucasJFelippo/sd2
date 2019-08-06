from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('home.html')


def main():
    app.env = 'development'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()