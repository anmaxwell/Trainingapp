  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from trainer.models import User, Training, Role, Level
import datetime

class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=120)])
    role = SelectField(u'Role', choices=[(1,"Business Analyst"),(2,"Test Engineer"),(3,"Developer")
                    ,(4,"Architect"),(5,"Product Owner"),(6,"Scrum Master")], coerce=int)     
    level = SelectField(u'Level', choices=[(1,"Apprentice"),(2,"Graduate"),(3,"Associate")
                    ,(4,"Mid"),(5,"Senior"),(6,"Principal")], coerce=int)     
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Login')

class Profile(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    role = SelectField(u'Role', choices=[(1,"Business Analyst"),(2,"Test Engineer"),(3,"Developer")
                    ,(4,"Architect"),(5,"Product Owner"),(6,"Scrum Master")], coerce=int)
    level = SelectField(u'Level', choices=[(1,"Apprentice"),(2,"Graduate"),(3,"Associate")
                    ,(4,"Mid"),(5,"Senior"),(6,"Principal")], coerce=int)
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