from datetime import datetime
from trainer import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    training = db.Column(db.Integer, db.ForeignKey('training.id'), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    level = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    review = db.Column(db.Text)
    user_id = db.relationship('User', backref='usertrain', lazy=True)

    def __repr__(self):
        return f"User('{self.provider}', '{self.title}')"

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    user_id = db.relationship('User', backref='userrole', lazy=True)

    def __repr__(self):
        return f"Role('{self.id}')"

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    user_id = db.relationship('User', backref='userlevel', lazy=True)

    def __repr__(self):
        return f"Level('{self.id}')"

