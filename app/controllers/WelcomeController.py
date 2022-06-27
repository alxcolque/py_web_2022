from flask import render_template


class WelcomeController():
    def __init__(self):
        pass
    def index(self):
        return render_template('welcome.html')
welcomecontroller = WelcomeController()