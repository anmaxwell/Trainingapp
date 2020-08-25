  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from trainer.models import User, Training


class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=120)])
    role = StringField('Role',
                        validators=[DataRequired(), Length(min=2, max=20)])                        
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Login')

class Profile(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    role = StringField('Role',
                            validators=[DataRequired(), Length(min=2, max=20)])
    level = StringField('Level',
                            validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Login')


class LogTraining(FlaskForm):
    provider = StringField('Provider',
                           validators=[DataRequired(), Length(max=20)])
    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=120)])
    date_taken = DateField('Date Entered', format='%Y-%m-%d')
    rating = SelectField(u'Rating', choices=[], coerce=int)
    review = TextAreaField('Review')
    submit = SubmitField('Login')