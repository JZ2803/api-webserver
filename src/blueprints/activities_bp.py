from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.activity import Activity, ActivitySchema
from models.enrolment import Enrolment

# Define the activities_bp Blueprint
activities_bp = Blueprint('activities', __name__, url_prefix="/activities")  # Create a Blueprint for the activities routes

# Define a route for creating a new activity
@activities_bp.route("/<int:enrolment_id>", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_activities(enrolment_id):  # Function to create a new activity
    db.get_or_404(Enrolment, enrolment_id)  # Get the enrolment with the given ID or return a 404 error
    activity_info = ActivitySchema(only=['date_performed', 'activity_type_id']).load(request.json, unknown='exclude')  # Load the activity information from the request JSON
    activity = Activity(
        date_performed=activity_info['date_performed'],
        activity_type_id=activity_info['activity_type_id'],
        enrolment_id=enrolment_id,
        user_id=get_jwt_identity()  # Get the user ID from the JWT token
    )  # Create a new activity object with the provided information
    db.session.add(activity)  # Add the activity to the database session
    db.session.commit()  # Commit the changes to the database
    return ActivitySchema(exclude=['user_id']).dump(activity), 201  # Return the created activity as JSON with a 201 status code

# Define a route for deleting an activity from the database
@activities_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id # Require JWT authentication for this route and user must be an admin
def delete_activity(id):
    activity = db.get_or_404(Activity, id)  # Get the activity with the given ID or return a 404 error
    db.session.delete(activity)  # Delete the activity from the database
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return a message indicating that the activity was deleted successfully