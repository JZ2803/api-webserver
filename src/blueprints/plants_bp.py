from init import db
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.plant import Plant, PlantSchema, PlantEnrolmentSchema

plants_bp = Blueprint('plants', __name__, url_prefix="/plants")

@plants_bp.route("/", methods=['GET'])
def get_all_plants():
    """Returns a list of all plant records including its specie and id of customer to whom it belongs."""
    stmt = db.select(Plant)
    plants = db.session.scalars(stmt).all()
    return PlantSchema(many=True).dump(plants)

@plants_bp.route("/<int:id>", methods=['GET'])
def get_plant(id):
    """Returns a list of all enrolments associated with a plant."""
    plant = db.get_or_404(Plant, id)
    return PlantEnrolmentSchema().dump(plant)