
# controllers/books.py
from ..models import Book


class BooksController:
    """
    Controller for multi-book operations: list, sort.
    """

    @staticmethod
    def get_books():
        """
        Return preview data for all books.
        """
        return Book.get_all()

    @staticmethod
    def validate_sort_parameters(params):
        """
        Validate query parameters for sorting books.
        """
        return Book.validate_sort_parameters(params)

    @staticmethod
    def get_books_sorted(params):
        """
        Return sorted preview data for all books.
        """
        return Book.sort_all(params)

