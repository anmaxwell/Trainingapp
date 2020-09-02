from trainer import app, db
from trainer.models import User, Training, Role, Level
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
            thisuser=User.query.filter_by(email=form.email.data).first()
            if thisuser == None:
                flash('Email not recognised', 'danger')
            else:
                session['logged_in'] = True
                session['name'] = form.email.data
                session['role'] = thisuser.userrole.id
                session['level'] = thisuser.userlevel.id
                return redirect(url_for('history'))
        else:
            flash('Login Unsuccessful. Please check email', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session['name'] = form.email.data
            thisuser=User.query.filter_by(email=form.email.data).first()
            if thisuser == None:
                session['role'] = form.role.data
                session['level'] = form.level.data
                newuser = User(email=form.email.data, role=form.role.data, level= form.level.data)
                db.session.add(newuser)
                db.session.commit()
                flash(f"Account created for {session['name']}!", 'success')
                return redirect(url_for('profile'))
            else:
                session['role'] = thisuser.userrole.id
                session['level'] = thisuser.userlevel.id
                flash(f"Account already exists for {session['name']}!", 'success')
                return redirect(url_for('history'))
        flash(f"Danger for {session['name']}!", 'danger')
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/profile')
def profile():
    form = Profile()
    if request.method == 'GET':
        if session.get('logged_in') == True:
            form.username.data = session['name']
            form.role.data = session['role']
            form.level.data = session['level']
        else:
            return redirect(url_for('login'))
    return render_template('profile.html', title='Profile', form=form, role=session['role'], level=session['level'])

@app.route('/logtraining')
def logtraining():
    form = LogTraining()
    return render_template('logtraining.html', title='LogTraining', form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    session['logged_in'] = False
    return redirect(url_for('index'))