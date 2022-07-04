from flask import render_template, request, redirect, url_for
from app import db, bcrypt, app
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
            email = request.form['username']
            password = request.form['password']
            return redirect(url_for('welcome_router.home'))
        return render_template('auth/signin.html')
authcontroller = AuthController()