from blueprints.cli_bp import db_commands
from init import app

app.register_blueprint(db_commands)

print(app.url_map)