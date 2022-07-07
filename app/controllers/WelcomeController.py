from flask import render_template
from app.models.Product import Product


class WelcomeController():
    def __init__(self):
        pass
    def index(self):
        products = Product.query.all() #select * from products;
        return render_template('welcome.html', products=products)
    def home(self):
        return render_template('home.html')
welcomecontroller = WelcomeController()