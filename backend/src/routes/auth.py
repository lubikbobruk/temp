from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from ..models import create_login_model, create_user_model
from ..controllers import AuthController


auth_namespace = Namespace("auth", description="Authentication related operations.")

login_model = create_login_model(auth_namespace)
user_model = create_user_model(auth_namespace)


@auth_namespace.route('/login')
class LoginRouter(Resource):
    """
    A resource representing the login route. Handles user authentication through the POST method.
    """

    @auth_namespace.expect(login_model)
    @auth_namespace.response(401, "Invalid login data")
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
        Logs in a user by verifying their email address and password.

        :return: A dictionary containing user data with the following keys:
                    - id (int): User ID.
                    - name (str): User's name.
                    - surname (str): User's surname.
                    - email (str): User's email.
                    - ratings (list[dict[str, any]]): Dictionary of user's movie ratings.
                    - access_token (str): User's JWT access token.
        :rtype: dict[str, any]
        """
        auth_controller = AuthController()

        login_data = request.get_json()

        if not auth_controller.login_user(login_data.get("user_email"), login_data.get("user_password")):
            return {"message": "Invalid login data"}, 401

        login_response = auth_controller.login_data()

        return login_response, 200


@auth_namespace.route('/logout')
class LogoutRouter(Resource):
    """
    A resource representing the logout route. Handles user logout operations through the GET method.
    """

    @jwt_required()
    def get(self):
        """
        Logs out the currently authenticated user.

        :return: A dictionary containing a "Successfully logged out." message.
        :rtype: dict[str, str]
        """
        logout_response = {"message": "Successfully logged out."}

        return logout_response, 200
