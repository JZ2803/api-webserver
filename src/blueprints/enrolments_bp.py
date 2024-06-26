from auth import admin_only_with_id
from datetime import date
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerSchema
from models.enrolment import Enrolment, EnrolmentSchema, EnrolmentNewCustomerSchema, EnrolmentSummarySchema
from models.plant import Plant, PlantSchema

enrolments_bp = Blueprint('enrolments', __name__, url_prefix="/enrolments")

@enrolments_bp.route("/new", methods=['POST'])
@jwt_required()
def create_enrolment_new():
    """Creates an enrolment, plant and customer record for a first-time customer and returns the newly created records."""
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')
    customer = Customer(
        first_name=customer_info['first_name'],
        last_name=customer_info['last_name'],
        email=customer_info['email'],
        phone_no=customer_info['phone_no']
    )
    db.session.add(customer)
    db.session.commit()
    
    plant_info = PlantSchema(only=['specie_id']).load(request.json, unknown='exclude')
    plant = Plant(
        specie_id=plant_info['specie_id'],
        customer_id=customer.id
    )
    db.session.add(plant)
    db.session.commit()

    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')
    enrolment = Enrolment(
        start_date=enrolment_info['start_date'],
        end_date=enrolment_info['end_date'],
        plant_id=plant.id
    )
    db.session.add(enrolment)
    db.session.commit()

    return EnrolmentNewCustomerSchema().dump(enrolment)

@enrolments_bp.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_enrolment_summary(id):
    """Returns the dates and plant associated with an enrolment and all comments and activities associated with the enrolment."""
    enrolment = db.get_or_404(Enrolment, id)
    return EnrolmentSummarySchema().dump(enrolment)

@enrolments_bp.route("/current", methods=['GET'])
@jwt_required()
def get_current_enrolments():
    """Returns a list of all current enrolments."""
    stmt = db.select(Enrolment).where(Enrolment.end_date > date.today())
    enrolments = db.session.scalar(stmt)
    return EnrolmentSchema().dump(enrolments)

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