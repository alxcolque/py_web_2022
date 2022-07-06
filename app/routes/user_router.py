from flask import Blueprint
from app.controllers.UserController import usercontroller


user_router = Blueprint('user_router', __name__)
@user_router.route('/users', methods=['GET'])
def index():
    return usercontroller.index()