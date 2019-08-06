from flask import Flask, render_template, request
from flask import Blueprint


formbp = Blueprint('formbp', __name__, template_folder='templates')


@formbp.route('/signin')
def index():
    return render_template('signin.html')