#coding=utf-8
from flask import Flask, request, render_template, redirect, url_for, flash, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, fresh_login_required
from Login_Handle import AuthChecking, LoginForm, LoginRoute
from Register_Handle import RegisterForm, AddUser, RegisterRoute


app = Flask(__name__, template_folder="templates")
app.register_blueprint(LoginRoute.login_app)
app.register_blueprint(RegisterRoute.register_app)
app.secret_key = "TFKUYGILUHCFHJTFKYG5768567"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = 'Unauthorized User'
login_manager.session_protection = "strong"
login_manager.login_message_category = "info"



class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(userid):
    curr_user = User()
    curr_user.id = userid
    return curr_user

@app.route('/mainpage')
@fresh_login_required
def mainpage():
    return render_template("index.html", username=current_user.get_id())

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_app.usrlogin'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/')
def homepage():
    return render_template("main.html")



if __name__ == '__main__':
    app.debug = True
    app.run()