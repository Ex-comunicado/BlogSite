from datetime import datetime
from enum import unique
from blogmain import bcrypt, login_manager
from wtforms.validators import Length
from blogmain import db
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plaintext_pass):
        self.password_hash = bcrypt.generate_password_hash(plaintext_pass).decode('utf-8')
    
    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class BlogPosts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=255))
    content = db.Column(db.Text())
    author = db.Column(db.String(length=255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(length=255))