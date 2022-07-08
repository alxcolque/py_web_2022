from sqlalchemy import TIMESTAMP, DateTime, text
from sqlalchemy.sql import func
from app import db
class Sale(db.Model):
    __tablename__="sales"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # foreign key
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id',ondelete="CASCADE"))

    status = db.Column(db.String(30))
    invoice = db.Column(db.String(1500), nullable=True)
    total = db.Column(db.Numeric(10,2), nullable=True)
    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    #relationship
    detalle=db.relationship('Detail', backref='sale', lazy='dynamic')