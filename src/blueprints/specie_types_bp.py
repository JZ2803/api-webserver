from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.specie import Specie
from models.specie_type import SpecieType, SpecieTypeSchema

specie_types_bp = Blueprint('specie_types', __name__, url_prefix="/specie_types")

@specie_types_bp.route("/", methods=['GET'])
def get_all_specie_types():
    stmt = db.select(SpecieType)
    specie_types = db.session.scalars(stmt).all()
    return SpecieTypeSchema(many=True).dump(specie_types)

@specie_types_bp.route("/", methods=['POST'])
@jwt_required()
def create_specie_type():
    specie_type_info = SpecieTypeSchema(only=['name']).load(request.json, unknown='exclude')
    specie_type = SpecieType(
        name=specie_type_info['name']
    )
    db.session.add(specie_type)
    db.session.commit()
    return SpecieTypeSchema().dump(specie_type), 201

@specie_types_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_specie_type(id):
    specie_type = db.get_or_404(SpecieType, id)

    stmt = db.select(Specie).where(Specie.specie_type_id == id)
    specie = db.session.scalar(stmt)

    if not specie:
        db.session.delete(specie_type)
        db.session.commit()
        return {'message': "Deleted successfully"}
    return {'error': "Cannot delete specie type as there are specie(s) associated with it"}, 400