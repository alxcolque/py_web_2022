__version__ = "0.1"
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import (_db_user,_db_name,_db_host,_db_pass,_upload_profile)
import secrets

app = Flask(__name__, template_folder="views") 
#conection db
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://{}:{}@{}/{}'.format(
 os.getenv('DB_USER', _db_user),
 os.getenv('DB_PASSWORD', _db_pass),
 os.getenv('DB_HOST', _db_host),
 os.getenv('DB_NAME', _db_name),
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY']=secret

app.debug = True

#conexion con las rutas
from app.routes.welcome_router import welcome_router
app.register_blueprint(welcome_router)

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.user_router import user_router
app.register_blueprint(user_router)
 