# controllers/auth.py
from ..models import User


class AuthController:
    """
    A class for user authentication.

    Responsible for logging users in and providing login data.
    """

    def __init__(self):
        self.user = None

    def login_user(self, user_email, user_password):
        """
        Authenticate a user by email and password.

        :return: True if credentials are valid, False otherwise.
        """
        self.user = User.get_by_email(user_email)
        return bool(self.user and self.user.validate_password(user_password))

    def login_data(self):
        """
        Return login data for the authenticated user, including JWT.
        """
        return self.user.get_login_data()
