from sqlalchemy import TIMESTAMP, DateTime, text
from flask_login import UserMixin
from sqlalchemy.sql import func
from app import db
class User(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(30))
    create_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    update_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))