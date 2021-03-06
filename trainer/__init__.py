import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#adding security to prevent XS forgery attacks etc.
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bcrypt = Bcrypt(app)

#creating the db in the same directory using ///
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

#test users
people = {'ania@ania.com': {'role': 'Architect', 'level': 'Mid'},
          'test@test.com': {'role': 'Product Owner', 'level': 'Senior'},
          'aniamaxwell@yahoo.com': {'role': 'Developer', 'level': 'Associate'}}


#to prevent getting stuck in circular imports create this last
from trainer import routes, models


