from trainer import app, db
from trainer.models import User, Training
from trainer.forms import SignUpForm, LoginForm, Profile, LogTraining
from flask import render_template, url_for, flash, redirect

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successful.', 'success')
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    flash('Danger for {form.username.data}!', 'danger')
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/profile')
def profile():
    form = Profile()
    return render_template('profile.html', title='Profile', form=form)

@app.route('/logtraining')
def logtraining():
    form = LogTraining()
    return render_template('logtraining.html', title='LogTraining', form=form)