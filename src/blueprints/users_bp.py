from auth import admin_only, admin_only2
from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from init import bcrypt, db
from models.user import User, UserSchema, UserSummarySchema

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

@users_bp.route("/", methods=['GET'])
@jwt_required()
def get_all_users():
    """Returns a list of all users in the database including id, email and admin status."""
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSummarySchema(many=True).dump(users)

@users_bp.route("/create", methods=['POST'])
@admin_only
def create_user():
    """Creates a new user in the database and returns such user record."""
    params = UserSchema(only=['email', 'password', 'is_admin']).load(request.json, unknown='exclude')
    user = User(
        email=params['email'],
        password=bcrypt.generate_password_hash(params['password']).decode('utf8'),
        is_admin=params['is_admin']
    )
    db.session.add(user)
    db.session.commit()

    return UserSchema().dump(user), 201

@users_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(id):
    """Updates a user's email and password and returns the updated record. Users can only make changes to their own email and password unless they are an admin."""
    user_to_update = db.get_or_404(User, id)
    
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)

    if user_id == user_to_update.id or user:
        params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
        user.email = params.get('email', user.email)
        user.password = params.get('password', user.password)

        db.session.commit()
        return UserSchema().dump(user)

    return {'error': "You don't have permission to update this user"}, 403

@users_bp.route("/<int:id>", methods=['DELETE'])
@admin_only2
def delete_user(id):
    """Deletes a user record from the database. This can only be performed by an admin."""
    user_to_delete = db.get_or_404(User, id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return {'message': "Deleted successfully"}