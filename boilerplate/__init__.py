import json
from flask import Flask

from boilerplate.views.home import home


def create_app(config_path="config.json"):
    app = Flask(__name__)  # instance_relative_config=True

    with open(config_path) as config_file:
        config = json.load(config_file)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db"
    app.config["SECRET_KEY"] = config["SECRET_KEY"]
    app.config['PORT'] = config["PORT"]
    app.config["DEBUG"] = config["DEBUG"]

    app.app_context().push()

    # Database instantiation
    from boilerplate.extensions import db
    db.init_app(app)
    db.create_all()

    # Register blueprints
    app.register_blueprint(home, url_prefix="")

    return app

