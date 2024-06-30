from blueprints.activities_bp import activities_bp
from blueprints.activity_types_bp import activity_types_bp
from blueprints.cli_bp import db_commands
from blueprints.comments_bp import comments_bp
from blueprints.customers_bp import customers_bp
from blueprints.enrolments_bp import enrolments_bp
from blueprints.plants_bp import plants_bp
from blueprints.specie_types_bp import specie_types_bp
from blueprints.species_bp import species_bp
from blueprints.users_bp import users_bp
from init import app
from marshmallow.exceptions import ValidationError

# Register all the blueprints with the Flask application
app.register_blueprint(activities_bp)
app.register_blueprint(activity_types_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(db_commands)
app.register_blueprint(enrolments_bp)
app.register_blueprint(plants_bp)
app.register_blueprint(specie_types_bp)
app.register_blueprint(species_bp)
app.register_blueprint(users_bp)

# Print the URL map of the Flask application
print(app.url_map)

# Define error handlers for specific HTTP status codes
@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': "Not found"}, 404

# Define error handler for validation errors
@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)["messages"]}, 400

# Define error handler for key errors
@app.errorhandler(KeyError)
def missing_key(err):
    return {"error": f"Missing field: {str(err)}"}, 400