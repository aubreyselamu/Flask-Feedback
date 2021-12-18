from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import RegisterForm, LoginForm

from models import connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flash_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = 'Yohanna_12'
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    return redirect('/register')

@app.route('/register', methods=["GET","POST"])
def register_user():
    '''Show user form and process form by adding a new user'''
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password,first_name,last_name,email)

        
        db.session.commit()
        session['username'] = user.username

        return redirect('/secret')
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    '''Show login form and process the login form'''

    form = LoginForm()

    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        user = User.authenticate(username,password)

        if user:
            session['username'] = user.username
            return redirect('/secret')
        else:
            form.username.errors = ['Invalid username/password']
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)




@app.route('/secret')
def secret():
    if 2==5:
        flash("Please login first")
        return redirect('/login')
    else:
        return "<h1>You made it!</h1>"

@app.route('/logout')
def logout_user():
    session.pop("username")
    return redirect('/login')

