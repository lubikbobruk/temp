from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api
from flask_migrate import Migrate

# point at our extensions package
from .exts import db
# import the refactored models
from .models import User, Book, Rating, Comment
# import the renamed routes
from .routes import auth_namespace, user_namespace, books_namespace

def create_app(config):
    """
    Creates and configures an instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    JWTManager(app)

    # set up REST-x with our namespaces
    api = Api(app, doc='/docs')
    api.add_namespace(auth_namespace)
    api.add_namespace(user_namespace)
    api.add_namespace(books_namespace)

    @app.shell_context_processor
    def make_shell_context():
        # what’s available in `flask shell`
        return {
            "db": db,
            "User": User,
            "Book": Book,
            "Rating": Rating,
            "Comment": Comment,
        }

    return app
