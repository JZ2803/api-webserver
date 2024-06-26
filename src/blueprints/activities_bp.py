from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.activity import Activity, ActivitySchema
from models.enrolment import Enrolment

activities_bp = Blueprint('activities', __name__, url_prefix="/activities")

@activities_bp.route("/<int:id>", methods=['POST'])
@jwt_required()
def create_activities(id):
    """Creates a new activity for an existing enrolment in the database and returns such record."""
    db.get_or_404(Enrolment, id)
    activity_info = ActivitySchema(only=['date_performed', 'activity_type_id']).load(request.json, unknown='exclude')
    activity = Activity(
        date_performed=activity_info['date_performed'],
        activity_type_id=activity_info['activity_type_id'],
        enrolment_id=id,
        user_id=get_jwt_identity()
    )
    db.session.add(activity)
    db.session.commit()
    return ActivitySchema().dump(activity), 201

@activities_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_activity(id):
    """Deletes an activity record from the database."""
    activity = db.get_or_404(Activity, id)
    db.session.delete(activity)
    db.session.commit()
    return {'message': "Deleted successfully"}