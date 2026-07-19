import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # Get the project root directory
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    app.config.from_object("config.Config")

    db.init_app(app)

    from app.routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app