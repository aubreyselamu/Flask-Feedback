from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from forms import FeedbackForm, RegisterForm, LoginForm
from werkzeug.exceptions import Unauthorized

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
        return render_template('users/register.html', form=form)

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
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password']
            return render_template('login.html', form=form)
    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout_user():
    '''Logout user'''

    session.pop("username")
    return redirect('/login')


@app.route('/users/<username>')
def show_user(username):
    '''Example page for logged-in-users'''

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.filter_by(username=username).first()



    return render_template('users/show.html', user=user)

@app.route('/users/<username>/delete', methods=["POST"])
def remove_user_feedback(username):
    '''Remove user and redirect to login'''
    if "username" not in session or username != session["username"]:
        raise Unauthorized()
    
    user = User.query.delete()
    db.session.delete(user)
    db.session.commit()
    session.pop("username")
    return redirect('/')


@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def add_feedback(username):
    '''Display feedback form and process'''

    if "username" not in session or username != session["username"]:
        raise Unauthorized()

    form = FeedbackForm()
    
    if form.validate_on_submit():
        title = form.title.data
        content=form.content.data

        feedback = Feedback(
            title=title,
            content=content,
            username=username)

        db.session.add(feedback)
        db.session.commit()

        return redirect(f'/users/{feedback.username}')

    else:
        return render_template('feedback/new.html', form=form)

@app.route('/feedback/<int:feedback_id>/update', methods=["GET", "POST"])
def edit_feedback(feedback_id):
    '''Display form to edit feedback'''

    feedback = Feedback.query.get_or_404(feedback_id)

    if "username" not in session or feedback.username != session["username"]:
        raise Unauthorized()

    form = FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()

        return redirect(f'users/{feedback.username}')
   
    return render_template('feedback/edit.html', form=form)


