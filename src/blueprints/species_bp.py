from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.specie import Specie, SpecieSchema
from models.specie_type import SpecieType

species_bp = Blueprint('species', __name__, url_prefix="/species")

@species_bp.route("/", methods=['GET'])
def get_all_species():
    """Returns a list of all species in the database."""
    stmt = db.select(Specie)
    species = db.session.scalars(stmt).all()
    return SpecieSchema(many=True).dump(species)

@species_bp.route("/<int:id>", methods=['POST'])
@jwt_required()
def create_specie(id):
    """Creates a new specie for an existing specie type in the database and returns created specie record."""
    db.get_or_404(SpecieType, id)
    specie_info = SpecieSchema(only=['name']).load(request.json, unknown='exclude')
    specie = Specie(
        name=specie_info['name'],
        specie_type_id=id
    )
    db.session.add(specie)
    db.session.commit()
    return SpecieSchema().dump(specie), 201

@species_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_specie(id):
    """Deletes a specie from the database."""
    specie = db.get_or_404(Specie, id)
    db.session.delete(specie)
    db.session.commit()
    return {'message': "Deleted successfully"}