from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerSchema

# Define a Blueprint for customers
customers_bp = Blueprint('customers', __name__, url_prefix="/customers")

# Define a route for getting all customers
@customers_bp.route("/", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_all_customers():
    stmt = db.select(Customer) # Query to select all records from the Customers table
    customers = db.session.scalars(stmt).all() # Execute query and retrieve the result
    return CustomerSchema(many=True).dump(customers) # Serialize retrieved records and return JSON object

# Define a route for getting a customer's plants
@customers_bp.route("/<id>", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_customer_plants(id):
    customer = db.get_or_404(Customer, id) # Retrieve customer record from database or raise 404 error if customer does not exist
    return CustomerSchema(only=['first_name', 'last_name', 'plants']).dump(customer) # Serialize retrieved records and return JSON object

# Define a route for creating a new customer
@customers_bp.route("/", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_customer():
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')  # Load the customer information from the request JSON using the CustomerSchema
    customer = Customer(
        first_name=customer_info['first_name'],
        last_name=customer_info['last_name'],
        email=customer_info['email'],
        phone_no=customer_info['phone_no']
    )  # Create a new Customer object with the provided information
    db.session.add(customer)  # Add the new customer to the database session
    db.session.commit()  # Commit the changes to the database
    return CustomerSchema().dump(customer), 201  # Return the newly created customer in JSON format and 201 status code

# Define a route for updating a customer
@customers_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()  # Require JWT authentication for this route
def update_customer(id):
    customer = db.get_or_404(Customer, id)  # Retrieve customer record from database or raise 404 error if customer does not exist
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')  # Load the customer information from the request JSON using the CustomerSchema
    # Update the customer's information
    customer.first_name = customer_info.get('first_name', customer.first_name)
    customer.last_name = customer_info.get('last_name', customer.last_name)
    customer.email = customer_info.get('email', customer.email)
    customer.phone_no = customer_info.get('phone_no', customer.phone_no)
    db.session.commit()  # Commit the changes to the database
    return CustomerSchema().dump(customer)  # Return the updated customer in JSON format

# Define a route for deleting a customer
@customers_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_customer(id):
    customer = db.get_or_404(Customer, id)  # Retrieve the customer from the database using its ID or return 404 error
    db.session.delete(customer)  # Delete the customer from the database
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return an error message indicating that the customer has been deleted