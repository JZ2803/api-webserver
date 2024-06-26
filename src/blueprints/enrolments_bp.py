from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.enrolment import Enrolment, EnrolmentSchema, EnrolmentSummarySchema
from models.plant import Plant

enrolments_bp = Blueprint('enrolments', __name__, url_prefix="/enrolments")

## RETURN ALL COMMETNS AND ACTIVITIES ASSOCIATED WITH AN ENROLMENT
@enrolments_bp.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_customer_plants(id):
    """Returns a list of all the comments and activities associated with an enrolment."""
    enrolment = db.get_or_404(Enrolment, id)
    return EnrolmentSummarySchema().dump(enrolment)

## GET ALL CURRENT ENROLMENTS

@enrolments_bp.route("/<int:id>", methods=['POST'])
@jwt_required()
def create_enrolment(id):
    """Creates a new enrolment for an existing plant in the database and returns created enrolment record."""
    db.get_or_404(Plant, id)
    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')
    enrolment = Enrolment(
        start_date=enrolment_info['start_date'],
        end_date=enrolment_info['end_date'],
        plant_id=id
    )
    db.session.add(enrolment)
    db.session.commit()
    return EnrolmentSchema().dump(enrolment), 201

@enrolments_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()
def update_enrolment(id):
    """Updates an existing enrolment and returns updated enrolment record."""
    enrolment = db.get_or_404(Enrolment, id)
    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')
    enrolment.start_date = enrolment_info.get('start_date')
    enrolment.end_date = enrolment_info.get('end_date')
    db.session.commit()
    return EnrolmentSchema().dump(enrolment)

@enrolments_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_enrolment(id):
    """Deletes an enrolment record from the database."""
    enrolment = db.get_or_404(Enrolment, id)
    db.session.delete(enrolment)
    db.session.commit()
    return {'message': "Deleted successfully"}