from flask import render_template
from app.models.Sale import Sale
class SaleController():
    def __init__(self):
        pass
    def index(self):
        sales = Sale.query.all()
        return render_template('sales/index.html', sales=sales)

salecontroller = SaleController()