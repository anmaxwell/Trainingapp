from trainer import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('home.html')
    #return("Hello World!")
    