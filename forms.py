from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    '''Form for registering a user'''

    username=StringField("Username", validators=[InputRequired()])
    password=PasswordField("Password", validators=[InputRequired()])
    email=StringField("E-mail", validators=[InputRequired()])
    first_name=StringField("First Name", validators=[InputRequired()])
    last_name=StringField("Last Name", validators=[InputRequired()])

class LoginForm(FlaskForm):
    '''Form for logging in a user'''

    username=StringField("Username", validators=[InputRequired()])
    password=PasswordField("Password", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    '''Form for adding feedback'''
    title = StringField("Title", validators=[InputRequired()])
    password=StringField("Content", validators=[InputRequired()])
    