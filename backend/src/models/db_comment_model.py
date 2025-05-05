from ..exts import db


class Comment(db.Model):
    """
    The Comment class is a database model that represents a user's comment for a specific movie.

    :ivar id: Unique identifier for each comment.
    :type id: int

    :ivar movie_id: Identifier for the movie that the comment pertains to.
    :type movie_id: int

    :ivar user_id: Identifier for the user who made the comment.
    :type user_id: int

    :ivar comment: The text of the comment made by the user.
    :type comment: str
    """
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comment = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        """
        String representation of the Comment instance.

        :return: String representing the comment.
        :rtype: comment
        """
        return f"<Comment-{self.id}>"

    def save(self):
        """
        Save the current instance of Comment to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current instance of Comment from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def update_comment(self, new_comment):
        """
        Update the comment for the current instance.

        :param new_comment: The new comment value.
        :type new_comment: str
        """
        self.comment = new_comment
        db.session.commit()

    def get_user_id(self):
        """
        Get the unique identifier of the user.

        :return: User's ID.
        :rtype: int
        """
        return self.user_id

    def get_user_comment(self):
        """
        Get the comment of the user.

        :return: User's comment.
        :rtype: str
        """
        return self.comment

    @staticmethod
    def create(movie_id, user_id, comment):
        """
        Create a new Comment instance or if exists it will be updated.

        :param movie_id: Identifier for the movie that the comment pertains to.
        :type movie_id: int

        :param user_id: Identifier for the user who made the comment.
        :type user_id: int

        :param comment: The text of the comment made by the user.
        :type comment: str

        :return: A new Comment instance or updated existing instance.
        :rtype: comment
        """
        comment_update = Comment.query.filter_by(movie_id=movie_id, user_id=user_id).first()
        if comment_update is not None:
            comment_update.update_comment(comment)

            return comment_update

        return Comment(movie_id=movie_id, user_id=user_id, comment=comment)
