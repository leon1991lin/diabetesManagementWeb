from webProject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"

    #columns
    user_id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name       = db.Column(db.String(12))
    user_account    = db.Column(db.String(64), unique=True)
    user_password   = db.Column(db.String(128))
    born_date       = db.Column(db.Date)
    telephone       = db.Column(db.String(32))
    address         = db.Column(db.String(128))
    user_type       = db.Column(db.Integer)
    create_time     = db.Column(db.DateTime)
    update_time     = db.Column(db.DateTime)
    delete_time     = db.Column(db.DateTime)

    def __init__(self, name, account, password, born_date, telephone, address, user_type, create_time):

        self.user_name      = name
        self.user_account   = account
        self.user_password  = generate_password_hash(password) # save hashed password
        self.born_date      = born_date
        self.telephone      = telephone
        self.address        = address
        self.user_type      = user_type
        self.create_time    = create_time

#     def check_password(self, password):
#         return check_password_hash(self.user_password, password)
#
#     def get_id(self):
#         return (self.user_id)
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

