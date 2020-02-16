from trainer import app, db, bcrypt

@app.route('/')
def index():
    return("Hello World")