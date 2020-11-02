  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from trainer.models import User, Training, Role, Level, Interest
import datetime

class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=120)])
    role = SelectField(u'Role', choices=[], coerce=int)     
    level = SelectField(u'Level', choices=[], coerce=int)     
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Login')

class Profile(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=120)])
    role = SelectField(u'Role', choices=[], coerce=int)
    level = SelectField(u'Level', choices=[], coerce=int)
    #interests = BooleanField()
    interests = StringField('Interests')
    submit = SubmitField('Login')

class LogTraining(FlaskForm):
    provider = StringField('Provider',
                           validators=[DataRequired(), Length(max=20)])
    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=120)])
    date_taken = DateField('Date Taken', format='%Y-%m-%d', default=datetime.date.today)
    rating = SelectField(u'Rating', choices=[(1,"Definitely wouldn't recommend"),(2,"Wouldn't recommend"),(3,"Neutral")
                    ,(4,"Would recommend"),(5,"Definitely would recommend")], coerce=int)
    review = TextAreaField('Review')
    submit = SubmitField('Login')

class Admin(FlaskForm):
    role = StringField('Role',
                            validators=[Length(min=2, max=30)])
    level = StringField('Level',
                            validators=[Length(min=2, max=30)])
    discipline = SelectField(u'Discipline', choices=[], coerce=int)
    interest = StringField('Interest',
                            validators=[Length(min=2, max=30)])
    training = SelectField(u'Training', choices=[], coerce=int)
    submit = SubmitField('Submit')