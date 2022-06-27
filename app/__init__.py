__version__ = "0.1"
import os
from flask import Flask

app = Flask(__name__, template_folder="views") 
app.debug = True

#conexion con las rutas
from app.routes.welcome_router import welcome_router
app.register_blueprint(welcome_router)
 