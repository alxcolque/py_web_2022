from flask import flash, render_template, request, redirect, url_for
from app import db, bcrypt, app
from sqlalchemy import or_
from app.models.User import User
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
            role = 'cliente'
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
            
            return redirect(url_for('welcome_router.home'))
        return render_template('auth/signup.html')
    def signin(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter(or_(User.username == username, User.email == username)).first()
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    return redirect(url_for('welcome_router.home'))
                
            flash('Credenciales no válidos..!', 'danger')
            return redirect(url_for('auth_router.signin'))
        return render_template('auth/signin.html')
authcontroller = AuthController()