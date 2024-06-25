from init import db
from flask import Blueprint

enrolments_bp = Blueprint('enrolments', __name__, url_prefix="/enrolments")
