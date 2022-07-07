from flask import Blueprint
from app.controllers.SaleController import salecontroller


sale_router = Blueprint('sale_router', __name__)
@sale_router.route('/sales', methods=['GET'])
def index():
    return salecontroller.index()