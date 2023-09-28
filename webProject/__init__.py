import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask login
from flask_login import LoginManager

username="root"
password="0000"
host="localhost"
port="3306"
database_name="dmplat"

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY']= 'iamleonpro'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# load_user
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
