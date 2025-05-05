# controllers/book.py
from ..models import Book, Rating, Comment


class BookController:
    """
    Controller for single-book operations: retrieve, rate, comment.
    """

    def __init__(self, book_id):
        self.book = Book.get_by_id(book_id)

    def get_book(self):
        """
        Retrieve a book's full data by ID, or None if not found.
        """
        return None if self.book is None else self.book.get_data()

    def rate_book(self, user_id, user_rating):
        """
        Add or update a user's rating for this book.

        :return: Updated book data dict or None if book not found.
        """
        if not self.book:
            return None
        new_rating = Rating.create(self.book.get_id(), user_id, user_rating)
        new_rating.save()
        return self.book.get_data()

    def comment_book(self, user_id, user_comment):
        """
        Add or update a user's comment for this book.

        :return: Updated book data dict or None if book not found.
        """
        if not self.book:
            return None
        new_comment = Comment.create(self.book.get_id(), user_id, user_comment)
        new_comment.save()
        return self.book.get_data()

