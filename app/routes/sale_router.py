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

@sale_router.route('/cartitem/delete/<id>', methods=['GET'])
def deteleItem(id):
    return salecontroller.deteleItem(id)

@sale_router.route('/cartitem/quantity/<id>/<qu>', methods=['GET'])
def updatequantity(id, qu):
    return salecontroller.updateQuantity(id, qu)

@sale_router.route('/buyup', methods=['GET'])
def buyup():
    return salecontroller.buyUp()