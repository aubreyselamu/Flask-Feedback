from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

from models import connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Yohanna_12'
debug = DebugToolbarExtension(app)

connect_db(app)