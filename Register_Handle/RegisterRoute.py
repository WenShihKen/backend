#coding=utf-8
from flask import Flask, request, render_template, redirect, url_for, flash, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from Login_Handle import AuthChecking, LoginForm
from Register_Handle import RegisterForm, AddUser

register_app = Blueprint('register_app',__name__,"templates")

@register_app.route('/register', methods=['GET', 'POST'])
def usr_register():
    form = RegisterForm.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        if AddUser.SameUserCheck(form.username.data) == False:
            return render_template('register.html', error="account is exist", form=form)
        else:
            AddUser.InsertUser(form.username.data, form.password.data)

        return redirect(url_for('login_app.usrlogin'))
    return render_template('register.html', form=form)