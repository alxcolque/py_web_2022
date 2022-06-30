from flask import Blueprint
from app.controllers.AuthController import authcontroller


auth_router = Blueprint('auth_router', __name__)
@auth_router.route('/signup', methods=['GET'])
def signup():
    return authcontroller.signup()
    
@auth_router.route('/signin', methods=['GET'])
def signin():
    return authcontroller.signin()