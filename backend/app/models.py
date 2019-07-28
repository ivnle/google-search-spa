from . import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.String)

    def __repr__(self):
        return '<Post {}>'.format(self.name)


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    exercise = db.Column(db.String(128))
    pounds = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    rpe = db.Column(db.Integer)
    notes = db.Column(db.String(140))
    bodyweight = db.Column(db.Integer)

    def __repr__(self):
        return '<Set {}>'.format(self.exercise)


class SetSchema(ma.ModelSchema):
    class Meta:
        model = Set


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, default="my_username")
    email = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    sets = db.relationship('Set', backref='user', lazy='dynamic')

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password, method='sha256')

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return None

        return user


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User





class SetAnon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    exercise = db.Column(db.String(128))
    pounds = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    rpe = db.Column(db.Integer)
    notes = db.Column(db.String(140))
    bodyweight = db.Column(db.Integer)

    def __repr__(self):
        return '<SetAnon {}>'.format(self.exercise)


class SetAnonSchema(ma.ModelSchema):
    class Meta:
        model = SetAnon


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
