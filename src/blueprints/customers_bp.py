from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerSchema

customers_bp = Blueprint('customers', __name__, url_prefix="/customers")

@customers_bp.route("/", methods=['POST'])
@jwt_required()
def create_customer():
    """ Create a new customer in database"""
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json)
    customer = Customer(
        first_name=customer_info['first_name'],
        last_name=customer_info['last_name'],
        email=customer_info['email'],
        phone_no=customer_info['phone_no']
    )
    db.session.add(customer)
    db.session.commit()
    return CustomerSchema().dump(customer), 201
