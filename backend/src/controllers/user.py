# controllers/user.py
from ..models import User, Book


class UserController:
    """
    Controller for user-related operations: get data, recommendations, predictions.
    """

    def __init__(self, user_id):
        self.user = User.get_by_id(user_id)

    def get_data(self):
        """
        Retrieve user data dict, or None if user not found.
        """
        return None if not self.user else self.user.get_data()

    def get_recommendations(self):
        """
        Retrieve book recommendations for the user.
        """
        if not self.user:
            return None
        raw_recs = self.user.get_recommendations()
        return Book.format_recommendations(raw_recs)

    def get_predicted_book_rating(self, book_id):
        """
        Retrieve a predicted rating for a specified book.

        :return: Prediction dict or None if user/book not found.
        """
        if not self.user or not Book.get_by_id(book_id):
            return None
        return self.user.get_predicted_book_rating_by_book_id(book_id)
