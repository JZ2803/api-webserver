from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.plant import Plant, PlantSchema

# Define a Blueprint for plants
plants_bp = Blueprint('plants', __name__, url_prefix="/plants")

# Define a route for getting all plants
@plants_bp.route("/", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_all_plants():
    stmt = db.select(Plant)  # Query to select all records from the Plants table
    plants = db.session.scalars(stmt).all()  # Execute query and retrieve the result
    return PlantSchema(many=True).dump(plants)  # Serialize retrieved records and return JSON object


# Define a route for getting a plant's details
@plants_bp.route("/<int:id>", methods=['GET'])
@jwt_required()  # Require JWT authentication for this route
def get_plant(id):
    plant = db.get_or_404(Plant, id)  # Retrieve the plant from the database using its ID or return 404 error
    return PlantSchema(only=['id', 'specie', 'customer_id', 'enrolments']).dump(plant)  # Serialize retrieved records and return JSON object

# Define a route for creating a new plant
@plants_bp.route("/", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_plant():
    plant_info = PlantSchema(only=['specie_id', 'customer_id']).load(request.json, unknown='exclude')  # Load the plant information from the request JSON using the PlantSchema
    plant = Plant(
        specie_id=plant_info['specie_id'],
        customer_id=plant_info['customer_id']
    )  # Create a new Plant object with the provided information
    db.session.add(plant)  # Add the new plant to the database session
    db.session.commit()  # Commit the changes to the database
    return PlantSchema().dump(plant), 201  # Return the newly created plant in JSON format and 201 status code

# Define a route for deleting a plant
@plants_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_plant(id):
    plant = db.get_or_404(Plant, id)  # Retrieve the plant from the database using its ID or return 404 error
    db.session.delete(plant)  # Delete the plant from the database
    db.session.commit()  # Commit the changes to the database
    return {'message': "Deleted successfully"}  # Return an error message indicating that the plant has been deleted