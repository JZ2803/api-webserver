from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.enrolment import Enrolment, EnrolmentSchema
from models.plant import Plant

enrolments_bp = Blueprint('enrolments', __name__, url_prefix="/enrolments")

@enrolments_bp.route("/<int:id>", methods=['POST'])
@jwt_required()
def create_enrolment(id):
    """Creates a new enrolment for an existing plant in the database and returns created enrolment record."""
    plant = db.get_or_404(Plant, id)
    
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