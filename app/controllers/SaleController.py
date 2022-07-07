from flask import flash, redirect, render_template, url_for
from app.models.Sale import Sale
from app.models.Detail import Detail
from app import db, app
class SaleController():
    def __init__(self):
        pass
    def index(self):
        sales = Sale.query.all()
        return render_template('sales/index.html', sales=sales)
    def addcart(self, _id):
        if _id != '':
            sale = Sale(status = "carrito")
            db.session.add(sale)
            db.session.commit()
            
            detail=Detail(sale_id=sale.id,product_id=_id,quantity=1)
            db.session.add(detail)
            db.session.commit()
            flash('Producto añadido al carrito..!', 'success')
            return redirect(url_for('welcome_router.index'))
        
        return redirect(url_for('welcome_router.index'))
    def showcart(self):
        sales = Sale.query.all()
        return render_template('sales/mycart.html', sales=sales)
salecontroller = SaleController()