from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.activity import Activity
from models.activity_type import ActivityType, ActivityTypeSchema

# Define the activity_types_bp Blueprint
activity_types_bp = Blueprint('activity_types', __name__, url_prefix="/activity_types")  # Create a Blueprint for the activity types routes

# Define a route for getting all activity types
@activity_types_bp.route("/", methods=['GET'])  
def get_all_activity_types():  
    stmt = db.select(ActivityType)  # Construct a SQLAlchemy select statement to fetch all ActivityType records
    activity_types = db.session.scalars(stmt).all()  # Use the session's scalars method to fetch all ActivityType records
    return ActivityTypeSchema(many=True).dump(activity_types)  # Use the ActivityTypeSchema to serialize the fetched activity types into JSON format

# Define a route for creating a new activity type
@activity_types_bp.route("/", methods=['POST'])
@jwt_required() # Require JWT authentication for this route
def create_activity_type():
    activity_type_info = ActivityTypeSchema(only=['name']).load(request.json, unknown='exclude')  # Load the activity type information from the request JSON using the ActivityTypeSchema
    activity_type = ActivityType(
        name=activity_type_info['name']
    )  # Create a new ActivityType object with the provided name
    db.session.add(activity_type)  # Add the new activity type to the database session
    db.session.commit()  # Commit the changes to the database
    return ActivityTypeSchema().dump(activity_type), 201  # Return the newly created activity type in JSON format and 201 status code

# Define a route for deleting an activity type
@activity_types_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id # Require JWT authentication and user must be an admin
def delete_activity_type(id):
    activity_type = db.get_or_404(ActivityType, id)  # Get the activity type from the database using its ID or return 404 error

    stmt = db.select(Activity).where(Activity.activity_type_id == id)  # Construct a SQLAlchemy select statement to fetch any associated activities
    activity = db.session.scalar(stmt)  # Fetch the first associated activity from the database session

    if not activity:  # If there are no associated activities, delete the activity type and commit the changes to the database
        db.session.delete(activity_type)
        db.session.commit()
        return {'message': "Deleted successfully"}
    return {'error': "Cannot delete activity type as there are activity(s) associated with it"}, 400  # Otherwise, return an error message indicating that the activity type cannot be deleted because it has associated activities