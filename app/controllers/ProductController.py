from flask import render_template
from app.models.Product import Product
class ProductController():
    def __init__(self):
        pass
    def index(self):
        products = Product.query.all()
        return render_template('products/index.html', products=products)

productcontroller = ProductController()
