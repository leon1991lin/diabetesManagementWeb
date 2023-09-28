from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError,DateField, SelectField
from wtforms.validators import DataRequired, Email

# from webProject.models.models import User
from webProject.models.MedicalStaff import MedicalStaff

class LoginForm(FlaskForm):

    user_account = StringField('使用者帳號(信箱)', validators=[DataRequired(), Email()])
    user_password = PasswordField('使用者密碼', validators=[DataRequired()])
    submit = SubmitField('登入')

class RegistrationForm(FlaskForm):

    user_account    = StringField('使用者帳號(電子信箱)', validators=[DataRequired(), Email()])
    user_password   = PasswordField('使用者密碼', validators=[DataRequired()])
    user_name       = StringField('姓名', validators=[DataRequired()])
    user_type       = SelectField('職業業別', choices=[('1','醫師'),('2','護理師'),('3','營養師'), ('4','營養師'), ('5','個案管理師'), ('6','衛教師')])
    staff_position         = StringField('職稱',validators=[DataRequired()])
    submit = SubmitField('註冊')

    def check_account(self, field):

        if MedicalStaff.query.filter_by(staff_account=field.data).first():
        # if User.query.filter_by(user_account=field.data).first():
            raise ValidationError("此電子信箱已註冊過")

# class RegistrationForm(FlaskForm):
#
#     user_account    = StringField('使用者帳號(電子信箱)', validators=[DataRequired(), Email()])
#     user_password   = PasswordField('使用者密碼', validators=[DataRequired()])
#     user_name       = StringField('姓名', validators=[DataRequired()])
#     born_date       = DateField('出身年月日', format='%Y-%m-%d',validators=[DataRequired()])
#     telephone       = StringField('行動電話',validators=[DataRequired()])
#     address         = StringField('聯絡地址',validators=[DataRequired()])
#     user_type       = SelectField('你的角色', choices=[('1','病友'),('2','照護者')])
#     submit = SubmitField('註冊')
#
#     def check_account(self, field):
#
#         if User.query.filter_by(user_account=field.data).first():
#             raise ValidationError("此電子信箱已註冊過")
