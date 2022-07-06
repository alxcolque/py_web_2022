from sqlalchemy import TIMESTAMP, DateTime, text
from sqlalchemy.sql import func
from app import db
class Client(db.Model):
    __tablename__="clients"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    phone = db.Column(db.String(20))
    cinit = db.Column(db.String(30), unique=True)
    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))