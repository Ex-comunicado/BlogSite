from enum import unique
from flask import Flask, render_template, flash
from flask.sessions import NullSession
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mysqlusername:mysqlpassword@localhost/users" #replace mysqlusername with your mysql username and mysqlpassword with your mysql password
app.config['SECRET_KEY'] = "" #enter an encrypted key to generate anti-CSRF tokens

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from blogmain import routes
