from flask import Blueprint
from app.controllers.SaleController import salecontroller


sale_router = Blueprint('sale_router', __name__)
@sale_router.route('/sales', methods=['GET'])
def index():
    return salecontroller.index()

@sale_router.route('/addcart/<id>', methods=['GET'])
def addcart(id):
    return salecontroller.addcart(id)

@sale_router.route('/showcart', methods=['GET'])
def showcart():
    return salecontroller.showcart()