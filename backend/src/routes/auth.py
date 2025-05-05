from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from models.serialization_models import create_login_model, create_user_model
from controllers.auth import AuthController

auth_namespace = Namespace("auth", description="Authentication related operations.")

login_model = create_login_model(auth_namespace)
user_model = create_user_model(auth_namespace)


@auth_namespace.route('/login')
class LoginRouter(Resource):
    @auth_namespace.expect(login_model)
    @auth_namespace.response(401, "Invalid login data")
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
        POST /auth/login
        Validate user credentials and return user data + access token.
        """
        auth_controller = AuthController()
        data = request.get_json()

        if not auth_controller.login_user(data.get("user_email"), data.get("user_password")):
            return {"message": "Invalid login data"}, 401

        return auth_controller.login_data(), 200


@auth_namespace.route('/logout')
class LogoutRouter(Resource):
    @jwt_required()
    def get(self):
        """
        GET /auth/logout
        Simple logout endpoint (JWT protects it).
        """
        return {"message": "Successfully logged out."}, 200
