from flask import render_template
class AuthController():
    def __init__(self):
        pass
    
    def signup(self):
        return render_template('auth/signup.html')
    def signin(self):
        return render_template('auth/signin.html')
authcontroller = AuthController()