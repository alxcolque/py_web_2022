from flask import render_template, request, redirect, url_for
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
            if password != pass_conf:
                return "El campo de las contraseñas no coinciden...!"
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