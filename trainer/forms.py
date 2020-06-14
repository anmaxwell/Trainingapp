  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Profile(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    role = StringField('Role',
                            validators=[DataRequired(), Length(min=2, max=20)])
    Interest1 = BooleanField('Interest 1')
    Interest2 = BooleanField('Interest 2')
    Interest3 = BooleanField('Interest 3')
    Interest4 = BooleanField('Interest 4')
    Interest5 = BooleanField('Interest 5')
    Interest6 = BooleanField('Interest 6')
    Interest7 = BooleanField('Interest 7')
    Interest8 = BooleanField('Interest 8')
    Interest9 = BooleanField('Interest 9')
    Interest10 = BooleanField('Interest 10')
    Interest11 = BooleanField('Interest 11')
    Interest12 = BooleanField('Interest 12')
    submit = SubmitField('Login')


class LogTraining(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')