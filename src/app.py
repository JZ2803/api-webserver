from blueprints.activity_types_bp import activity_types_bp
from blueprints.cli_bp import db_commands
from blueprints.activities_bp import activities_bp
from blueprints.activity_types_bp import activity_types_bp
from blueprints.comments_bp import comments_bp
from blueprints.customers_bp import customers_bp
from blueprints.enrolments_bp import enrolments_bp
from blueprints.plants_bp import plants_bp
from blueprints.species_bp import species_bp
from blueprints.specie_types_bp import specie_types_bp
from blueprints.users_bp import users_bp
from init import app
from marshmallow.exceptions import ValidationError

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(plants_bp)
app.register_blueprint(enrolments_bp)
app.register_blueprint(activity_types_bp)
app.register_blueprint(species_bp)
app.register_blueprint(specie_types_bp)
app.register_blueprint(activities_bp)
app.register_blueprint(comments_bp)

print(app.url_map)

@app.route("/")
def hello_world():
    return "Hello World"

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    """ Handles 405 and 404 errors.

    Parameters:
        err (Exception): The exception object raised.

    Returns:
        dict: An error message and HTTP status code 404.
    """
    return {'error': "Not found"}, 404

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)["messages"]}, 400

@app.errorhandler(KeyError)
def missing_key(err):
    return {"error": f"Missing field: {str(err)}"}, 400