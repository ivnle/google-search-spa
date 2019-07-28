from flask import render_template, flash, redirect, url_for, jsonify, request, Blueprint, jsonify, current_app
from . import app, db
from .models import Post, PostSchema, User, SetAnon, SetAnonSchema, Set, SetSchema
from functools import wraps
from datetime import datetime, timedelta
import jwt
import sys


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@app.route('/search', methods=['GET'])
def search():
    data = request.args.get("name")
    post = Post.query.filter(
        Post.name.contains(data))  # .order_by(Post.some_field).all() use for ranking exercise variations
    output = PostSchema(many=True).dump(post).data
    return jsonify(output)


@app.route('/sets/', methods=['GET', 'POST'])
@token_required
def sets(current_user):
    if request.method == 'GET':
        return jsonify("hello, this is /sets from flask")
    elif request.method == 'POST':
        data = request.get_json()
        print(data, file=sys.stderr)
        _set = Set(
            user=current_user,
            exercise=data['exercise'],
            pounds=data['weight'],
            reps=data['reps'],
            rpe=data['rpe'],
            notes=data['notes'],
            bodyweight=data['bodyweight']
        )
        db.session.add(_set)
        db.session.commit()
        return "set saved", 201


@app.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return "registration success", 201


@app.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})


