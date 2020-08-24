from trainer import app, db, userlist
from trainer.models import User, Training
from trainer.forms import SignUpForm, LoginForm, Profile, LogTraining
from flask import render_template, url_for, flash, redirect, request, session

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data in userlist:
                session['name'] = form.email.data
                flash(f"Login successful for {session['name']}!", 'success')
                return redirect(url_for('history'))
            else:
                flash('Email not recognised', 'danger')
        else:
            flash('Login Unsuccessful. Please check email', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            session['name'] = form.email.data
            if form.email.data in userlist:
                flash(f"Account already exists for {session['name']}!", 'success')
                return redirect(url_for('history'))
            else:
                username = session['name']
                userlist.append(username)
                flash(f"Account created for {session['name']}!", 'success')
                return redirect(url_for('profile'))
        flash(f"Danger for {session['name']}!", 'danger')
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/profile')
def profile():
    form = Profile()
    return render_template('profile.html', title='Profile', form=form)

@app.route('/logtraining')
def logtraining():
    form = LogTraining()
    return render_template('logtraining.html', title='LogTraining', form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    return redirect(url_for('index'))