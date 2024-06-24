from blueprints.cli_bp import db_commands
from blueprints.customers_bp import customers_bp
from blueprints.users_bp import users_bp
from init import app
from marshmallow.exceptions import ValidationError

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(customers_bp)

print(app.url_map)

@app.route("/")
def hello_world():
    return "Hello World"

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': "Not found"}, 404

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)["messages"]}, 400


@app.errorhandler(KeyError)
def missing_key(err):
    return {"error": f"Missing field: {str(err)}"}, 400