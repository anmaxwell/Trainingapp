from trainer import app
from trainer.forms import SignUpForm, LoginForm
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('home.html')
    
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)