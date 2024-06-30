from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.plant import Plant
from models.specie import Specie, SpecieSchema
from models.specie_type import SpecieType, SpecieTypeSchema
from models.specie_type import SpecieType

# Define a Blueprint for species
species_bp = Blueprint('species', __name__, url_prefix="/species")

# Define a route for getting all species
@species_bp.route("/", methods=['GET'])
def get_all_species():
    stmt = db.select(Specie)  # SQLAlchemy statement to select all Specie records
    species = db.session.scalars(stmt).all()   # Execute the statement and get all Specie records
    return SpecieSchema(many=True).dump(species)  # Convert the Specie records to a JSON list of SpecieSchema objects

# Define a route for creating a new specie
@species_bp.route("/<int:specie_type_id>", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_specie(specie_type_id):
    db.get_or_404(SpecieType, specie_type_id)  # Get the SpecieType record with the provided id, or return a 404 error if it doesn't exist
    specie_info = SpecieSchema(only=['name']).load(request.json, unknown='exclude')  # Load the JSON data from the request into a SpecieSchema object, only including the 'name' field
    specie = Specie(
        name=specie_info['name'],
        specie_type_id=specie_type_id
    )  # Create a new Specie record with the provided name and specie_type_id
    db.session.add(specie)  # Add the new Specie record to the database session
    db.session.commit()  # Commit the changes to the database
    return SpecieSchema().dump(specie), 201  # Return the newly created Specie record as a JSON object with a 201 status code

# Define a route for deleting a specie
@species_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_specie(id):
    specie = db.get_or_404(Specie, id)  # Get the Specie record with the provided id, or return a 404 error if it doesn't exist

    stmt = db.select(Plant).where(Plant.specie_id == id)  # SQLAlchemy statement to select all Plant records associated with the Specie record
    plant = db.session.scalar(stmt)  # Execute the statement and get the first Plant record associated with the Specie record

    # If no plant is associated with the deleted specie, delete the specie
    if not plant:
        db.session.delete(specie)
        db.session.commit()
        return {'message': "Deleted successfully"}
    # If there is a plant associated with the deleted specie, return an error message
    return {'error': "Cannot delete specie as there are plant(s) associated with it"}, 400