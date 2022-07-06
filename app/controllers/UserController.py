from flask import render_template
from app.models.User import User
class UserController():
    def __init__(self):
        pass
    def index(self):
        users = User.query.all()
        return render_template('users/index.html', users=users)

usercontroller = UserController()