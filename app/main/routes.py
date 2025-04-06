from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/portal')
@login_required
def portal():
    return render_template('portal.html', user=current_user)

@main.route('/project1')
def project1():
    return render_template('project1.html')

@main.route('/project2')
def project2():
    return render_template('project2.html')

@main.route('/project3')
def project3():
    return render_template('project3.html')
