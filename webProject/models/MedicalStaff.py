from webProject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class MedicalStaff(db.Model, UserMixin):

    __tablename__ = "medical_staff"

    #columns
    staff_id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_name          = db.Column(db.String(12))
    staff_account       = db.Column(db.String(64), unique=True)
    staff_password      = db.Column(db.String(128))
    staff_position_code = db.Column(db.Integer)
    staff_position      = db.Column(db.String(32))
    create_time         = db.Column(db.DateTime)
    update_time         = db.Column(db.DateTime)
    delete_time         = db.Column(db.DateTime)

    def __init__(self, name, account, password, staff_position_code, staff_position, create_time):

        self.staff_name      = name
        self.staff_account   = account
        self.staff_password  = generate_password_hash(password) # save hashed password
        self.staff_position_code      = staff_position_code
        self.staff_position = staff_position
        self.create_time    = create_time

    def check_password(self, password):
        return check_password_hash(self.staff_password, password)

    def get_id(self):
        return (self.staff_id)

@login_manager.user_loader
def load_user(staff_id):
    return MedicalStaff.query.get(staff_id)

"""
@login_manager.user_loader 的實作為:

    def user_loader(self, callback):
        self.user_callback = callback
        return callback
"""