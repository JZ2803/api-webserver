from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.specie import Specie
from models.specie_type import SpecieType, SpecieTypeSchema

# Define a Blueprint for specie types
specie_types_bp = Blueprint('specie_types', __name__, url_prefix="/specie_types")

# Define a route for getting all specie types
@specie_types_bp.route("/", methods=['GET'])
def get_all_specie_types():
    stmt = db.select(SpecieType)  # Query to select all records from the SpecieType table
    specie_types = db.session.scalars(stmt).all()  # Execute query and retrieve the result
    return SpecieTypeSchema(many=True).dump(specie_types)  # Serialize retrieved records and return JSON object

# Define a route for creating a new specie type
@specie_types_bp.route("/", methods=['POST'])
@jwt_required()  # Require JWT authentication for this route
def create_specie_type():
    specie_type_info = SpecieTypeSchema(only=['name']).load(request.json, unknown='exclude')  # Load the specie type information from the request JSON using the SpecieTypeSchema
    specie_type = SpecieType(
        name=specie_type_info['name']
    )  # Create a new SpecieType object with the provided information
    db.session.add(specie_type)  # Add the new specie type to the database session
    db.session.commit()  # Commit the changes to the database
    return SpecieTypeSchema().dump(specie_type), 201  # Return the newly created specie type in JSON format and 201 status code

# Define a route for deleting a specie type
@specie_types_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id  # Require JWT authentication for this route and user must be an admin
def delete_specie_type(id):
    specie_type = db.get_or_404(SpecieType, id)  # Retrieve the specie type from the database using its ID or return 404 error

    stmt = db.select(Specie).where(Specie.specie_type_id == id)  # Query to select all records from the Specie table where the specie type ID matches the deleted specie type
    specie = db.session.scalar(stmt)  # Execute query and retrieve the result

    # If no specie is associated with the deleted specie type, delete the specie type
    if not specie:
        db.session.delete(specie_type)
        db.session.commit()
        return {'message': "Deleted successfully"}
    # If there is a specie associated with the deleted specie type, return an error message
    return {'error': "Cannot delete specie type as there are specie(s) associated with it"}, 400