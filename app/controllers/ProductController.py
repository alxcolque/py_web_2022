from flask import flash, render_template, request, redirect, url_for, session
from app.models.Product import Product
from app import db, app
class ProductController():
    def __init__(self):
        pass
    def index(self):
        products = Product.query.all()
        return render_template('products/index.html', products=products)
    def create(self):
        return render_template('products/create.html')
    def store(self):
        if request.method == 'POST':
            description = request.form['description']
            price = request.form['price']
            type = request.form['type']
            
            new_product = Product(
                description = description,
                type = type,
                price = price
            )
            db.session.add(new_product)
            db.session.commit()

            flash('Registro exitoso..!', 'success')
            return redirect(url_for('product_router.index'))
        return render_template('products/create.html')
    def edit(self, _id):
        product = db.session.query(Product).filter(Product.id==_id).one()
        return render_template('products/edit.html', product=product)
    def destroy(self, _id):
        product = db.session.query(Product).filter(Product.id==_id).one()
        db.session.delete(product)
        db.session.commit()
        flash('Producto eilminado con éxito..!', 'success')
        return redirect(url_for('product_router.index'))
    def update(self, _id):
        if request.method == 'POST':
            description = request.form['description']
            price = request.form['price']
            type = request.form['type']

            product = db.session.query(Product).filter(Product.id==_id).one()
            
            product.description = description,
            product.type = type,
            product.price = price
            db.session.commit()

            flash('Registro actualizado exitosamente..!', 'success')
            return redirect(url_for('product_router.index'))
        return '404 Método no válido'

productcontroller = ProductController()
