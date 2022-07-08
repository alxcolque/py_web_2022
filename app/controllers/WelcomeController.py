from flask import render_template
from app.models.Product import Product
from app.models.Image import Image


class WelcomeController():
    def __init__(self):
        pass
    def index(self):
        products = Product.query\
            .join(Image, Product.id==Image.product_id)\
            .all()
        return render_template('welcome.html', products=products)
    def home(self):
        return render_template('home.html')
welcomecontroller = WelcomeController()