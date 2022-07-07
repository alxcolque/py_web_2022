from flask import Blueprint
from app.controllers.ProductController import productcontroller


product_router = Blueprint('product_router', __name__)
@product_router.route('/products', methods=['GET'])
def index():
    return productcontroller.index()