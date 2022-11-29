from flask import Flask, render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    moment.init_app(app)

    # importing blueprints
    from .main import main as main_blueprint
   
    app.register_blueprint(main_blueprint)

    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    return app