from sqlalchemy import TIMESTAMP, DateTime, text
from sqlalchemy.sql import func
from app import db
class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    type = db.Column(db.String(50))
    description = db.Column(db.String(1500), nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=True)

    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))