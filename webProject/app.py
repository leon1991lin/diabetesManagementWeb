import datetime

from flask import render_template, redirect, request, url_for, flash
from  flask_login import login_user, logout_user, login_required

from webProject import app, db
from webProject.models.models import User
from webProject.models.MedicalStaff import MedicalStaff
from webProject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # user = User.query.filter_by(user_account=form.user_account.data).first()
        user = MedicalStaff.query.filter_by(staff_account=form.user_account.data).first()

        if (user is not None) and (user.check_password(form.user_password.data)):

            login_user(user)
            flash("您已成功登入!")

            next = request.args.get('next')

            if (next == None) or (next[0]!='/'):
                next = url_for('welcome_user')
            return redirect(next)

        else:

            flash('Wrong Email or Password')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已登出系統')
    return redirect(url_for('home'))

@app.route('/register',  methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        print("registing....")
        user = User(
            name=form.user_name.data,
            account=form.user_account.data,
            password=form.user_password.data,
            born_date=form.born_date.data,
            telephone=form.telephone.data,
            address=form.address.data,
            user_type=form.user_type.data,
            create_time=datetime.datetime.now()
        )
        print(user)
        db.session.add(user)
        db.session.commit()
        flash("感謝您的註冊")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/home')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/diabetes')
@login_required
def diabetes_home():
    return render_template('diabetes_home.html')


if __name__ == '__main__':
    app.run(debug=True, port="8668")