from flask import render_template


class WelcomeController():
    def __init__(self):
        pass
    def index(self):
        colores = {'color1':'negro','color2':'blanco','color3':'rojo'}
        saludo = "hola cómo estás?"
        return render_template('welcome.html', colores=colores, saludo = saludo)
    def home(self):
        return render_template('home.html')
welcomecontroller = WelcomeController()