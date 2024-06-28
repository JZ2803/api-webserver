from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerPlantSchema, CustomerSchema

customers_bp = Blueprint('customers', __name__, url_prefix="/customers")

@customers_bp.route("/", methods=['GET'])
@jwt_required()
def get_all_customers():
    stmt = db.select(Customer) # Query to select all records from the Customers table
    customers = db.session.scalars(stmt).all() # Execute query and retrieve the result
    return CustomerSchema(many=True).dump(customers) # Serialize retrieved records and return JSON object

@customers_bp.route("/<id>", methods=['GET'])
@jwt_required()
def get_customer_plants(id):
    customer = db.get_or_404(Customer, id) # Retrieve customer record from database or raise 404 error if customer does not exist
    return CustomerPlantSchema().dump(customer) # Serialize retrieved records and return JSON object

@customers_bp.route("/", methods=['POST'])
@jwt_required()
def create_customer():
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
    customer = db.get_or_404(Customer, id)
    db.session.delete(customer)
    db.session.commit()
    return {'message': "Deleted successfully"}