from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.activity_type import ActivityType, ActivityTypeSchema

activity_types_bp = Blueprint('activity_types', __name__, url_prefix="/activity_types")

@activity_types_bp.route("/", methods=['GET'])
def get_all_activity_types():
    """Returns a list of all activity type records."""
    stmt = db.select(ActivityType)
    activity_types = db.session.scalars(stmt).all()
    return ActivityTypeSchema(many=True).dump(activity_types)

@activity_types_bp.route("/", methods=['POST'])
@jwt_required()
def create_activity_type():
    """Creates a new activity type in the database and returns such record."""
    activity_type_info = ActivityTypeSchema(only=['name']).load(request.json, unknown='exclude')
    activity_type = ActivityType(
        name=activity_type_info['name']
    )
    db.session.add(activity_type)
    db.session.commit()
    return ActivityTypeSchema().dump(activity_type), 201

@activity_types_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_activity_type(id):
    """Deletes an activity type from the database."""
    activity_type = db.get_or_404(ActivityType, id)
    db.session.delete(activity_type)
    db.session.commit()
    return {'message': "Deleted successfully"}