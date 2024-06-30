from init import db
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required

# Define a decorator function for admin-only access
def admin_only(fn):
    # Wrap the provided function with a decorator that checks if the user is an admin
    @jwt_required()  # Require JWT authentication
    def inner():
        user_id = get_jwt_identity()  # Get the user ID from the JWT token
        stmt = db.select(User).where(User.id == user_id, User.is_admin)  # SQLAlchemy statement to select the User record with the provided user ID and is_admin flag
        user = db.session.scalar(stmt)  # Execute the statement and get the first User record with the provided user ID and is_admin flag

        if user:  # If the User record exists and the user is an admin
            return fn()  # Return the result of the provided function
        return {'error': "You must be an admin to access this resource"}, 403  # Return a JSON object with an error message and a 403 status code
    
    return inner  # Return the inner function as the result of the decorator

# Define a decorator function for admin-only access with a specific ID parameter
def admin_only_with_id(fn):
    # Wrap the provided function with a decorator that checks if the user is an admin and has the specified ID parameter
    @jwt_required()  # Require JWT authentication
    def inner_with_id(id):
        user_id = get_jwt_identity()  # Get the user ID from the JWT token
        stmt = db.select(User).where(User.id == user_id, User.is_admin)  # SQLAlchemy statement to select the User record with the provided user ID and is_admin flag
        user = db.session.scalar(stmt)  # Execute the statement and get the first User record with the provided user ID and is_admin flag
        if user:  # If the User record exists and the user is an admin
            return fn(id)  # Return the result of the provided function with the specified ID parameter
        return {'error': "You must be an admin to access this resource"}, 403  # Return a JSON object with an error message and a 403 status code
    
    return inner_with_id  # Return the inner_with_id function as the result of the decorator