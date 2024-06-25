from auth import admin_only_with_id
from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.specie_type import SpecieType, SpecieTypeSchema

specie_types_bp = Blueprint('specie_types', __name__, url_prefix="/specie_types")

@specie_types_bp.route("/", methods=['GET'])
def get_all_specie_types():
    """Returns a list of all specie type records."""
    stmt = db.select(SpecieType)
    activity_types = db.session.scalars(stmt).all()
    return SpecieTypeSchema(many=True).dump(activity_types)

@specie_types_bp.route("/", methods=['POST'])
@jwt_required()
def create_specie_type():
    """Creates a new specie type in the database and returns such record."""
    activity_type_info = SpecieTypeSchema(only=['name']).load(request.json, unknown='exclude')
    activity_type = SpecieType(
        name=activity_type_info['name']
    )
    db.session.add(activity_type)
    db.session.commit()
    return SpecieTypeSchema().dump(activity_type), 201

@specie_types_bp.route("/<int:id>", methods=['DELETE'])
@admin_only_with_id
def delete_specie_type(id):
    """Deletes a specie type from the database."""
    specie_type = db.get_or_404(SpecieType, id)
    db.session.delete(specie_type)
    db.session.commit()
    return {'message': "Deleted successfully"}