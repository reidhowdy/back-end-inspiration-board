from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel

    from app.models.board import Board
    from app.models.card import Card

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .card_routes import cards_bp
    app.register_blueprint(cards_bp)

    from .board_routes import boards_bp
    app.register_blueprint(boards_bp)

    CORS(app)
    return app
