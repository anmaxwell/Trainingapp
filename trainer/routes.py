from trainer import app, db, userlist, people
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
            if form.email.data in people:
                session['name'] = form.email.data
                session['role'] = people[session['name']]['role']
                session['level'] = people[session['name']]['level']
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
            session['role'] = form.role.data
            session['level'] = form.level.data
            if form.email.data in people:
                flash(f"Account already exists for {session['name']}!", 'success')
                return redirect(url_for('history'))
            else:
                newuser = {session['name']: {'role': session['role'], 'level': session['level']}}
                people.update(newuser)
                flash(f"Account created for {session['name']}!", 'success')
                return redirect(url_for('profile'))
        flash(f"Danger for {session['name']}!", 'danger')
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/profile')
def profile():
    form = Profile()
    if request.method == 'GET':
        form.username.data = session['name']
        form.role.data = session['role']
        form.level.data = session['level']
    return render_template('profile.html', title='Profile', form=form, role=session['role'], level=session['level'])

@app.route('/logtraining')
def logtraining():
    form = LogTraining()
    return render_template('logtraining.html', title='LogTraining', form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    return redirect(url_for('index'))