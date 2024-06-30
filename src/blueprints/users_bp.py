from auth import admin_only, admin_only_with_id
from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from init import bcrypt, db
from models.user import User, UserSchema, UserSummarySchema

# Define a Blueprint for users
users_bp = Blueprint('users', __name__, url_prefix="/users")

# Define a route for user login to obtain JWT
@users_bp.route("/login", methods=['POST'])
def login():
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')  # Load the JSON data from the request into a UserSchema object, only including the 'email' and 'password' fields
    
    stmt = db.select(User).where(User.email == params['email'])  # SQLAlchemy statement to select the User record with the provided email
    user = db.session.scalar(stmt)  # Execute the statement and get the first User record with the provided email

    if user and bcrypt.check_password_hash(user.password, params['password']):  # If the User record exists and the provided password matches the hashed password
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1.5))  # Create a JWT access token with the user's ID and an expiration time of 1.5 hours
        return {'token': token}  # Return the JWT access token as a JSON object
    return {'error': "Invalid email or password"}, 401  # Return a JSON object with an error message and a 401 status code if the email or password is invalid

# Define a route to retrieve a list of all users
@users_bp.route("/", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_all_users():
    stmt = db.select(User)  # SQLAlchemy statement to select all User records
    users = db.session.scalars(stmt).all()  # Execute the statement and get all User records
    return UserSummarySchema(many=True).dump(users)  # Convert the User records to a JSON list of UserSummarySchema objects

# Define a route to create a new user
@users_bp.route("/", methods=['POST'])
@admin_only  # Require JWT authentication for this route and user must be an admin
def create_user():
    params = UserSchema(only=['email', 'password', 'is_admin']).load(request.json, unknown='exclude')  # Load the JSON data from the request into a UserSchema object, only including the 'email', 'password', and 'is_admin' fields
    user = User(
        email=params['email'],
        password=bcrypt.generate_password_hash(params['password']).decode('utf8'),  # Create a hashed password using bcrypt
        is_admin=params['is_admin']
    )  # Create new user object using loaded data
    db.session.add(user)  # Add the new User record to the database session
    db.session.commit()  # Commit the changes to the database

    return UserSchema().dump(user), 201  # Return the newly created User record as a JSON object with a 201 status code

# Define a route to delete a user
@users_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_user(id):
    user_to_delete = db.get_or_404(User, id) # Get the User record with the provided id, or return a 404 error if it doesn't exist
    db.session.delete(user_to_delete)  # Delete the User record
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return a JSON object with a success message and a 200 status code