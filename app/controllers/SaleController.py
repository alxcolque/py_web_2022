from flask_login import current_user
from flask import flash, redirect, render_template, url_for
from app.models.Product import Product
from app.models.Sale import Sale
from app.models.Detail import Detail
from app.models.Client import Client
from app import db, app
class SaleController():
    def __init__(self):
        pass
    def index(self):
        sales = Sale.query.all()
        return render_template('sales/index.html', sales=sales)
    def addcart(self, _id):
        if _id != '':
            client = db.session.query(Client).filter(Client.user_id==current_user.id).first()
            if(bool(db.session.query(Sale).filter(Sale.status=='CARRITO', Sale.client_id==client.id).first())):
                sale = db.session.query(Sale).filter(Sale.status=='CARRITO').filter(Sale.client_id==client.id).first()
                detail=Detail(sale_id=sale.id,product_id=_id,quantity=1)
                db.session.add(detail)
                db.session.commit()
            else:
                sale = Sale(status = "CARRITO", client_id=client.id)
                db.session.add(sale)
                db.session.commit()
                
                detail=Detail(sale_id=sale.id,product_id=_id,quantity=1)
                db.session.add(detail)
                db.session.commit()
            flash('Producto añadido al carrito..!', 'success')
            return redirect(url_for('welcome_router.index'))
        
        return redirect(url_for('welcome_router.index'))
    def showcart(self):
        client = db.session.query(Client).filter(Client.user_id==current_user.id).first()
        detail = Detail.query\
            .join(Product, Product.id==Detail.product_id)\
            .join(Sale, Sale.id==Detail.sale_id)\
            .filter(Sale.client_id==client.id)\
            .filter(Sale.status=='CARRITO')\
            .all()
        suma = 0
        for row in detail:
            suma = suma + row.product.price*row.quantity
        
        return render_template('sales/mycart.html', detail=detail, total=suma)
    def deteleItem(self, _id):
        detail = Detail.query.get(_id)
        db.session.delete(detail)
        db.session.commit()
        flash('Item eliminado con éxito..!', 'success')
        return redirect(url_for('sale_router.showcart'))
    def updateQuantity(self,_id, qu):
        detail = Detail.query.get(_id)
        detail.quantity = qu
        db.session.commit()
        #flash('Item eliminado con éxito..!', 'success')
        return "ok"
    def buyUp(self):
        client = db.session.query(Client).filter(Client.user_id==current_user.id).first()
        if(bool(db.session.query(Sale).filter(Sale.status=='CARRITO', Sale.client_id==client.id).first())):
            sale = db.session.query(Sale).filter(Sale.status=='CARRITO').filter(Sale.client_id==client.id).first()
            sale.status = 'PENDIENTE'
            db.session.commit()
        flash('Pedido realizado con éxito..!', 'success')
        return redirect(url_for('sale_router.showcart'))
    #Methods for admin
    def showDetail(self, sale_id):
        sale = db.session.query(Sale).filter(Sale.id==sale_id).first()
        detail = Detail.query\
            .join(Product, Product.id==Detail.product_id)\
            .join(Sale, Sale.id==Detail.sale_id)\
            .filter(Detail.sale_id==sale_id)\
            .all()
        suma = 0
        for row in detail:
            suma = suma + row.product.price*row.quantity
        
        return render_template('sales/saledetail.html', detail=detail, total=suma, sale=sale)
    def confirmSale(self, _id):
        sale = db.session.query(Sale).filter(Sale.id==_id).filter(Sale.status=='PENDIENTE').first()
        sale.status = 'ACEPTADO'
        db.session.commit()
        return redirect(url_for('sale_router.index'))

salecontroller = SaleController()