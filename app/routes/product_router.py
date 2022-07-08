from flask import Blueprint
from app.controllers.ProductController import productcontroller


product_router = Blueprint('product_router', __name__)
@product_router.route('/products', methods=['GET'])
def index():
    return productcontroller.index()

@product_router.route('/products/create', methods=['GET'])
def create():
    return productcontroller.create()

@product_router.route('/products/store', methods=['POST'])
def store():
    return productcontroller.store()
@product_router.route('/products/delete/<id>', methods=['GET'])
def destroy(id):
    return productcontroller.destroy(id)
@product_router.route('/products/edit/<id>', methods=['GET'])
def edit(id):
    return productcontroller.edit(id)
@product_router.route('/products/editimage/<id>', methods=['GET'])
def editimage(id):
    return productcontroller.editimage(id)
@product_router.route('/products/update/<id>', methods=['POST'])
def update(id):
    return productcontroller.update(id)
@product_router.route('/product/addimage',methods=['POST'])
def storeImage():
    return productcontroller.storeImage()