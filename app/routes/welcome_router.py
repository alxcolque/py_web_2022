from flask import Blueprint
from app.controllers.WelcomeController import welcomecontroller


welcome_router = Blueprint('welcome_router', __name__)
@welcome_router.route('/', methods=['GET'])
def index():
    return welcomecontroller.index()
@welcome_router.route('/home', methods=['GET'])
def home():
    return welcomecontroller.home()