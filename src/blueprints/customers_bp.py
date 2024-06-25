from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerPlantSchema, CustomerSchema

customers_bp = Blueprint('customers', __name__, url_prefix="/customers")

@customers_bp.route("/", methods=['GET'])
@jwt_required()
def get_all_customers():
    """Returns a list of all customer records in the database including their id and contact details."""
    stmt = db.select(Customer)
    customers = db.session.scalars(stmt).all()
    return CustomerSchema(many=True).dump(customers)

@customers_bp.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_customer_plants(id):
    """Returns a list of all the plants belonging to a customer and respective enrolment date(s)."""
    customer = db.get_or_404(Customer, id)
    return CustomerPlantSchema().dump(customer)

@customers_bp.route("/", methods=['POST'])
@jwt_required()
def create_customer():
    """Creates a new customer in the database and returns such record."""
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')
    customer = Customer(
        first_name=customer_info['first_name'],
        last_name=customer_info['last_name'],
        email=customer_info['email'],
        phone_no=customer_info['phone_no']
    )
    db.session.add(customer)
    db.session.commit()
    return CustomerSchema().dump(customer), 201

@customers_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()
def update_customer(id):
    """Updates an existing customer's details and returns updated record."""
    customer = db.get_or_404(Customer, id)
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')
    customer.first_name = customer_info.get('first_name', customer.first_name)
    customer.last_name = customer_info.get('last_name', customer.last_name)
    customer.email = customer_info.get('email', customer.email)
    customer.phone_no = customer_info.get('phone_no', customer.phone_no)
    db.session.commit()
    return CustomerSchema().dump(customer)

@customers_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_customer(id):
    """Deletes a customer record from the database."""
    customer = db.get_or_404(Customer, id)
    db.session.delete(customer)
    db.session.commit()
    return {'message': "Deleted successfully"}