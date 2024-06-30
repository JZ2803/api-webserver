from auth import admin_only_with_id
from datetime import date
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.customer import Customer, CustomerSchema
from models.enrolment import Enrolment, EnrolmentSchema, EnrolmentNewCustomerSchema
from models.plant import Plant, PlantSchema

# Define a Blueprint for enrolments
enrolments_bp = Blueprint('enrolments', __name__, url_prefix="/enrolments")

# Define a route for creating a new enrolment with a new customer and plant
@enrolments_bp.route("/new", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_enrolment_new():
    customer_info = CustomerSchema(only=['first_name', 'last_name', 'email', 'phone_no']).load(request.json, unknown='exclude')  # Load the customer information from the request JSON using the CustomerSchema
    customer = Customer(
        first_name=customer_info['first_name'],
        last_name=customer_info['last_name'],
        email=customer_info['email'],
        phone_no=customer_info['phone_no']
    )  # Create a new Customer object with the provided information
    db.session.add(customer)  # Add the new customer to the database session
    db.session.commit()  # Commit the changes to the database
    
    plant_info = PlantSchema(only=['specie_id']).load(request.json, unknown='exclude')  # Load the plant information from the request JSON using the PlantSchema
    plant = Plant(
        specie_id=plant_info['specie_id'],
        customer_id=customer.id
    )  # Create a new Plant object with the provided information and the new customer's ID
    db.session.add(plant)  # Add the new plant to the database session
    db.session.commit()  # Commit the changes to the database

    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')  # Load the enrolment information from the request JSON using the EnrolmentSchema
    enrolment = Enrolment(
        start_date=enrolment_info['start_date'],
        end_date=enrolment_info['end_date'],
        plant_id=plant.id
    )  # Create a new Enrolment object with the provided information and the new plant's ID
    db.session.add(enrolment)  # Add the new enrolment to the database session
    db.session.commit()  # Commit the changes to the database

    return EnrolmentNewCustomerSchema().dump(enrolment)  # Return the newly created enrolment in JSON format

# Define a route for getting an enrolment summary
@enrolments_bp.route("/<int:id>", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_enrolment_summary(id):
    enrolment = db.get_or_404(Enrolment, id)  # Retrieve the enrolment from the database using its ID or return 404 error
    return EnrolmentSchema().dump(enrolment)  # Serialize retrieved records and return JSON object

# Define a route for getting the current enrolments
@enrolments_bp.route("/current", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_current_enrolments():
    stmt = db.select(Enrolment).where(Enrolment.end_date > date.today())   # Query to select all records from the Enrolments table where the end_date is greater than the current date
    enrolments = db.session.scalars(stmt).all()  # Execute query and retrieve the result
    return EnrolmentSchema(many=True, exclude=['activities', 'comments']).dump(enrolments)  # Serialize retrieved records and return JSON object

# Define a route for creating a new enrolment for an existing plant
@enrolments_bp.route("/<int:plant_id>", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_enrolment(plant_id):
    db.get_or_404(Plant, plant_id)  # Retrieve the plant from the database using its ID or return 404 error
    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')  # Load the enrolment information from the request JSON using the EnrolmentSchema
    enrolment = Enrolment(
        start_date=enrolment_info['start_date'],
        end_date=enrolment_info['end_date'],
        plant_id=plant_id
    )  # Create a new Enrolment object with the provided information and the provided plant's ID
    db.session.add(enrolment)  # Add the new enrolment to the database session
    db.session.commit()  # Commit the changes to the database
    return EnrolmentSchema(exclude=['activities', 'comments']).dump(enrolment), 201  # Return the newly created enrolment in JSON format and 201 status code

# Define a route for updating an enrolment
@enrolments_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()  # Require JWT authentication for this route
def update_enrolment(id):
    enrolment = db.get_or_404(Enrolment, id)  # Retrieve the enrolment from the database using its ID or return 404 error
    enrolment_info = EnrolmentSchema(only=['start_date', 'end_date']).load(request.json, unknown='exclude')  # Load the enrolment information from the request JSON using the EnrolmentSchema
    # Update the enrolment's information
    enrolment.start_date = enrolment_info.get('start_date')  
    enrolment.end_date = enrolment_info.get('end_date')
    db.session.commit()  # Commit the changes to the database
    return EnrolmentSchema(exclude=['activities', 'comments']).dump(enrolment)  # Return the updated enrolment in JSON format

# Define a route for deleting an enrolment
@enrolments_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_enrolment(id):
    enrolment = db.get_or_404(Enrolment, id)  # Retrieve the enrolment from the database using its ID or return 404 error
    db.session.delete(enrolment)  # Delete the enrolment from the database
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return an error message indicating that the enrolment has been deleted