from ..models import User


class AuthController:
    """
    A class for user authentication.

    This class is responsible for logging users in by verifying their email address and password.
    Once authenticated, the class provides access to the user's login data.

    :ivar user: A User object representing the currently logged-in user. Initially set to None.
    :type user: user
    """

    def __init__(self):
        self.user = None

    def login_user(self, user_email, user_password):
        """
        Logs in a user by verifying their email address and password.

        :param user_email: The email address of the user.
        :type user_email: str

        :param user_password: The password of the user.
        :type user_password: str

        :return: True if the email and password match a user in the database, False otherwise.
        :rtype: bool
        """
        self.user = User.get_by_email(user_email)
        return True if self.user and self.user.validate_password(user_password) else False

    def login_data(self):
        """
        Gets the login data for the authenticated user.

        :return: A dictionary containing:
                    - id (int): User ID.
                    - name (str): User name.
                    - surname (str): User surname.
                    - email (str): User email.
                    - ratings (list[dict[str, any]]): Dictionary of user's movie ratings.
                    - access token (str): JWT access token.
        :rtype: dict[str, any]
        """
        return self.user.get_login_data()
