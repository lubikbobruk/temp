from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restx import Api
from flask_migrate import Migrate

from .exts import db
from .models import User, Movie, Comment, Rating
from .routes import auth_namespace, user_namespace, movies_namespace


def create_app(config):
    """
    Creates and configures an instance of the Flask application.

    :param config: The configuration object to use.
    :type config: A configuration class (defined in a separate .py file)

    :return: A configured Flask application instance.
    :rtype: Flask
    """

    app = Flask(__name__)
    app.config.from_object(config)  # Load configurations from the config object.

    db.init_app(app)  # Initialize the database with the app.
    Migrate(app, db)  # Enable database migration features.
    CORS(app, supports_credentials=True, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    JWTManager(app)  # Initialize the JWT Manager.

    api = Api(app, doc='/docs')  # Initialize the API and set the doc route.
    # Add namespaces (which are essentially routes) to the API.
    api.add_namespace(auth_namespace)
    api.add_namespace(user_namespace)
    api.add_namespace(movies_namespace)

    @app.shell_context_processor
    def make_shell_context():
        """
        Provides shell context for the Flask application. This function will run every time the Flask shell is run.
        The context provided will be available in the shell.

        :return: A dictionary with the database instance and models.
        :rtype: dict
        """
        return {"db": db, "User": User, "Movie": Movie, "Comment": Comment, "Rating": Rating}

    return app
