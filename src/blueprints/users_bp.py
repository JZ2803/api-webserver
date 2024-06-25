from auth import admin_only
from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from init import bcrypt, db
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix="/users")

@users_bp.route("/login", methods=['POST'])
def login():
    """Returns an access token for a user."""
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1.5))
        return {'token': token}
    return {'error': "Invalid email or password"}, 401

# TO BE COMPLETED
@users_bp.route("/create", methods=['POST'])
@admin_only
def create_user():
    """Creates a new user in the database and returns such user record."""
    params = UserSchema(only=['email', 'password', 'is_admin']).load(request.json)
    user = User(
        email=params['email'],
        password=bcrypt.generate_password_hash(params['password']).decode('utf8'),
        is_admin=params['is_admin']
    )
    db.session.add(user)
    db.session.commit()

    return UserSchema().dump(user), 201
