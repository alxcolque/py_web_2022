from sqlalchemy import TIMESTAMP, DateTime, text
from sqlalchemy.sql import func
from app import db
class Detail(db.Model):
    __tablename__="details"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # foreign key
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id',ondelete="CASCADE"))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id',ondelete="CASCADE"))
    quantity = db.Column(db.Numeric(10,2), nullable=True)
    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))