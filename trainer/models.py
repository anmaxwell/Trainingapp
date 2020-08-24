from datetime import datetime
from trainer import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    training = db.relationship('Training', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.provider}', '{self.title}')"