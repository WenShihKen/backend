#coding=utf-8
from flask import Flask, request, render_template, redirect, url_for, flash, Blueprint
from Login_Handle import AuthChecking, LoginForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import main

login_app = Blueprint('login_app',__name__,"templates")

@login_app.route('/login', methods=['GET','POST'])
def usrlogin():
    error = None
    form = LoginForm.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if AuthChecking.LoginCheck(form.username.data, form.password.data):
            now_user = main.User()
            now_user.id = form.username.data
            login_user(now_user, remember=True)
            flash("Login Success")
            next = request.args.get('next')
            return redirect(next or url_for('mainpage'))
        else:
            error = 'Wrong Name or Password'
    return render_template('login.html', error=error, form=form)