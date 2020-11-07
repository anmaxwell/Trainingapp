from datetime import datetime
from trainer import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    training = db.relationship('Training', backref='usertrain', lazy=True)
    role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    level = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    interests = db.relationship('Interest', secondary = 'link')

    def __repr__(self):
        return f"User('{self.email}')"

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    date_taken = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    rating = db.Column(db.String(60), nullable=False)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Training('{self.provider}', '{self.title}')"

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    user_id = db.relationship('User', backref='userrole', lazy=True)

    def __repr__(self):
        return f"Role('{self.title}')"

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(30), unique=True, nullable=False)
    user_id = db.relationship('User', backref='userlevel', lazy=True)

    def __repr__(self):
        return f"Level('{self.id}')"

class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    discipline = db.Column(db.Integer, db.ForeignKey('discipline.id'), nullable=False)
    users = db.relationship('User',secondary='link')

    def __repr__(self):
        return f"Interest('{self.discipline}, {self.name}')"

class Discipline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    interest_id = db.relationship('Interest', backref='discint', lazy=True)

    def __repr__(self):
        return f"Discipline('{self.name}')"

class Link(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'), primary_key = True)