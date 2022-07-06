from sqlalchemy import TIMESTAMP, DateTime, text
from sqlalchemy.sql import func
from app import db
class Image(db.Model):
    __tablename__="images"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # foreign key
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    invoice = db.Column(db.String(150), nullable=True)
    status = db.Column(db.String(30), nullable=True)
    
    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))