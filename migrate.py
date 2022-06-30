from app.models.User import User
from app import db, bcrypt, app
def insertUser():
    id=1
    name='Alex Col'
    username='alec'
    email='a.colq3.c@gmail.com'
    password = bcrypt.generate_password_hash('asdfñlkj')
    role='admin'
    user = User(
        id=id,
        name=name,
        username=username,
        email=email,
        password=password,
        role=role
    )
    db.session.add(user)
    db.session.commit()
db.drop_all()
db.create_all()
insertUser()

