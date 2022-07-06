from flask import flash, render_template, request, redirect, url_for, session
from app import db, bcrypt, app
from flask_login import LoginManager, login_user, logout_user, current_user
from sqlalchemy import or_
from app.models.User import User
from app.models.Client import Client

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_router.signin'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class AuthController():
    def __init__(self):
        pass
    
    def signup(self):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            pass_conf = request.form['confirm-password']
            role = 'client'
            if password != pass_conf:
                return "El campo de las contraseñas no coinciden...!"
            password1 = bcrypt.generate_password_hash(password)
            new_user = User(
                name = name,
                username = username,
                email = email,
                password = password1,
                role = role
            )
            db.session.add(new_user)
            db.session.commit()

            new_client = Client(user_id = new_user.id, phone = '')
            db.session.add(new_client)
            db.session.commit()
            flash('Registro exitoso..!', 'success')
            return redirect(url_for('auth_router.signin'))
        return render_template('auth/signup.html')
    def signin(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter(or_(User.username == username, User.email == username)).first()
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    login_user(user)
                    if user.role == 'client':
                        return redirect(url_for('welcome_router.index'))
                    else:
                        return redirect(url_for('welcome_router.home'))
                
            flash('Credenciales no válidos..!', 'danger')
            return redirect(url_for('auth_router.signin'))
        return render_template('auth/signin.html')
    def logout(self):
        session.clear()
        logout_user()
        flash('Se ha cerrado la sesión', 'danger')
        return redirect(url_for('auth_router.signin'))
authcontroller = AuthController()