from trainer import app, db
from trainer.models import User, Training, Role, Level, Interest
from trainer.forms import SignUpForm, LoginForm, Profile, LogTraining, Admin
from flask import render_template, url_for, flash, redirect, request, session

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    if session.get('name') == None:
        return redirect(url_for('login'))
    thisuser=User.query.filter_by(email=session['name']).first()
    records=Training.query.filter_by(user_id=thisuser.id).order_by(Training.date_taken.desc())
    return render_template('history.html', title='History', records=records)

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
                return redirect(url_for('logtraining'))
        else:
            flash('Login Unsuccessful. Please check email', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    form.role.choices = [(role.id, role.title) for role in Role.query.order_by(Role.title).all()]
    form.level.choices = [(level.id, level.level) for level in Level.query.order_by(Level.level).all()]
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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = Profile()
    form.role.choices = [(role.id, role.title) for role in Role.query.order_by(Role.title).all()]
    form.level.choices = [(level.id, level.level) for level in Level.query.order_by(Level.level).all()]
    if session.get('name') == None:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        if session.get('logged_in') == True:
            allinterests=Interest.query.all()
            thisuser=User.query.filter_by(email=session['name']).first()
            form.username.data = session['name']
            form.role.data = thisuser.role
            form.level.data = thisuser.level
            userinterests=thisuser.interests
            return render_template('profile.html', title='Profile', form=form, allinterests=allinterests, userinterests=userinterests)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        if form.validate_on_submit():
            thisuser=User.query.filter_by(email=session['name']).first()
            thisuser.email = form.username.data
            thisuser.role = form.role.data
            thisuser.level = form.level.data
            db.session.add(thisuser)
            db.session.commit()
    return render_template('profile.html', title='Profile', form=form)

@app.route('/logtraining', methods=['GET', 'POST'])
def logtraining():
    form = LogTraining()
    if session.get('name') == None:
        return redirect(url_for('login'))
    if request.method == 'POST':
        thisuser=User.query.filter_by(email=session['name']).first()
        if form.validate_on_submit():
            newtrain = Training(provider=form.provider.data, title=form.title.data, date_taken=form.date_taken.data, rating=form.rating.data, review=form.review.data, user_id=thisuser.id)
            db.session.add(newtrain)
            db.session.commit()
            flash(f"Training created for {form.provider.data}!", 'success')
            return redirect(url_for('history'))
        else:
            flash(f"oh dear", 'danger')
    return render_template('logtraining.html', title='LogTraining', form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    session['logged_in'] = False
    return redirect(url_for('index'))

@app.route('/trainedit/<int:train_id>/update', methods=['GET', 'POST'])
def train_edit(train_id):
    form = LogTraining()
    if session.get('name') == None:
        return redirect(url_for('login'))
    trainedit=Training.query.get(train_id)
    thisuser=User.query.filter_by(email=session['name']).first()
    if request.method == 'GET':
        form.provider.data = trainedit.provider
        form.title.data = trainedit.title
        form.date_taken.data = trainedit.date_taken
        form.rating.data = trainedit.rating
        form.review.data = trainedit.review
    elif request.method == 'POST':
        if form.validate_on_submit():
            trainedit.provider = form.provider.data 
            trainedit.title = form.title.data 
            trainedit.date_taken = form.date_taken.data 
            trainedit.rating = form.rating.data 
            trainedit.review = form.review.data
            db.session.add(trainedit)
            db.session.commit()
            flash(f"Training update!", 'success')
            return redirect(url_for('history'))
        else:
            flash(f"oh dear", 'danger')
    return render_template('logtraining.html', title='LogTraining', form=form)
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # admin page to delete items, add roles or levels
    form = Admin()
    form.training.choices = [(train.id, train.title) for train in Training.query.order_by(Training.date_taken).all()]
    form.discipline.choices = [(disc.id, disc.discipline) for disc in Interest.query.all()]
    #if session.get('name') == None:
    #    return redirect(url_for('login'))
    #if session.get('name') != 'aniamaxwell@yahoo.com':
    #    flash(f"No Admin Access", 'danger')
    #    return redirect(url_for('profile'))
    
    if request.method == 'POST':
        if request.form['submit_button'] == 'AddRole':
            if Role.query.filter_by(title=form.role.data).count() == 0:
                newrole=Role(title=form.role.data)
                db.session.add(newrole)
                db.session.commit()
                flash(f"Added Role {form.role.data}", 'success')
            else:
                flash(f"{form.role.data} already exists", 'danger')

        elif request.form['submit_button'] == 'AddLevel':
            if Level.query.filter_by(level=form.level.data).count() == 0:
                newlevel=Level(level=form.level.data)
                db.session.add(newlevel)
                db.session.commit()
                flash(f"Added Level {form.level.data}", 'success')
            else:
                flash(f"{form.level.data} already exists", 'danger')

        elif request.form['submit_button'] == 'AddInterest':
            if Interest.query.filter_by(name=form.interest.data).count() == 0:
                newinterest=Interest(discipline=form.discipline.data, name=form.interest.data)
                db.session.add(newinterest)
                db.session.commit()
                flash(f"Added Interest {form.interest.data}", 'success')
            else:
                flash(f"{form.interest.data} already exists", 'danger')

        elif request.form['submit_button'] == 'Trainlist':
            return redirect(url_for('train_edit', train_id=form.training.data))       

    return render_template('admin.html', title='Admin', form=form)


@app.route('/trainlist')
def trainlist():
    if session.get('name') == None:
        return redirect(url_for('login'))
    records=Training.query.order_by(Training.date_taken.desc())
    return render_template('trainlist.html', title='Training', records=records)