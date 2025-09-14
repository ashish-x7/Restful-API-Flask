from flask import render_template, redirect, url_for
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))
