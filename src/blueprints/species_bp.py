from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.specie import Specie, SpecieSchema
from models.specie_type import SpecieType, SpecieTypeSchema
from models.specie_type import SpecieType

species_bp = Blueprint('species', __name__, url_prefix="/species")

@species_bp.route("/", methods=['GET'])
def get_all_species():
    stmt = db.select(Specie)
    species = db.session.scalars(stmt).all()
    return SpecieSchema(many=True).dump(species)

@species_bp.route("/<int:specie_type_id>", methods=['POST'])
@jwt_required()
def create_specie(specie_type_id):
    db.get_or_404(SpecieType, specie_type_id)
    specie_info = SpecieSchema(only=['name']).load(request.json, unknown='exclude')
    specie = Specie(
        name=specie_info['name'],
        specie_type_id=specie_type_id
    )
    db.session.add(specie)
    db.session.commit()
    return SpecieSchema().dump(specie), 201

@species_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_specie(id):
    specie = db.get_or_404(Specie, id)
    db.session.delete(specie)
    db.session.commit()
    return {'message': "Deleted successfully"}