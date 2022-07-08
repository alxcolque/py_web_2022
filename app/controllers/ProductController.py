from flask import flash, render_template, request, redirect, url_for, session
from app.models.Product import Product
from app.models.Product import Product
from app.models.Image import Image as UserPhoto
from flask_login import current_user
from app import db, app
from app.config import (_upload_profile)

import time
from PIL import Image #pip install pillow
from io import BytesIO
from base64 import b64decode
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
    def editimage(self, _id):
        images = db.session.query(UserPhoto).filter(UserPhoto.product_id==_id).all()
        product = db.session.query(Product).filter(Product.id==_id).one()
        return render_template('products/addimage.html', product=product, images=images)
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
    def destroy(self, _id):
        product = db.session.query(Product).filter(Product.id==_id).one()
        db.session.delete(product)
        db.session.commit()
        flash('Producto eliminado con éxito..!', 'success')
        return redirect(url_for('product_router.index'))
    def storeImage(self):
        if request.method == 'POST':
            product_id = request.form['product_id']
            base64_str = request.form.get('file')
            if base64_str == '':
                return 'No se ha selecciona ningún archivo para subir.'

            img = Image.open(BytesIO(b64decode(base64_str.split(',')[1])))
            url_current = time.strftime("%Y%m%d%H%M%S")
            img.save(_upload_profile+product_id+'-'+url_current+'.png')

            profile_actives = UserPhoto.query.filter(UserPhoto.status == 1).all()
            if profile_actives:
                for row in profile_actives:
                    row.status = 0
                    db.session.commit()

            profileimage = UserPhoto(product_id=product_id, url=product_id+'-'+url_current+'.png', status=1)
            db.session.add(profileimage)
            db.session.commit()
            
            return 'ok'
        return redirect(url_for('user_router.profile'))

productcontroller = ProductController()
