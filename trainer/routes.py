from trainer import app
from trainer.forms import SignUpForm, LoginForm, Profile, LogTraining
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
    form = Profile()
    return render_template('profile.html', form=form)

@app.route('/editprofile')
def editprofile():
    form = Profile()
    return render_template('profile.html', form=form)

@app.route('/logtraining')
def logtraining():
    form = LogTraining()
    return render_template('logtraining.html', form=form)