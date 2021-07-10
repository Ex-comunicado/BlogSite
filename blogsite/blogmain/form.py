from werkzeug.datastructures import ContentRange
from wtforms.widgets.core import TextArea
from blogmain.models import Users
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from blogmain import app

class NameForm(FlaskForm):
    name = StringField("Enter your name: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    def validate_username(self, user_to_check):
        usercheck = Users.query.filter_by(username=user_to_check.data).first()
        if usercheck:
            raise ValidationError('Username Already exists.')
    
    def validate_email_addr(self, email_addr_to_check):
        emailcheck = Users.query.filter_by(email=email_addr_to_check.data).first()
        if emailcheck:
            raise ValidationError('Email Address already exists.')

    username = StringField("Username: ",validators=[DataRequired(), Length(min=2, max=30)])
    email_addr = StringField("E-mail Address: ",validators=[DataRequired(), Email()])
    password1 = PasswordField("Password: ", validators=[Length(min=6), DataRequired()]) 
    password2 = PasswordField("Confirm Password: ",validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField("Create Account")

class LoginForm(FlaskForm):
    username = StringField("Username: ",validators=[DataRequired()])
    password =  PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Sign in")

class BlogPostForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    content = StringField("Content: ", validators=[DataRequired()], widget=TextArea())
    author = StringField("Author: ", validators=[DataRequired()])
    slug = StringField("Slug: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
