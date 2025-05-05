from ..exts import db


class Rating(db.Model):
    """
    The Rating class is a database model that represents a user's rating for a specific movie.

    :ivar id: Unique identifier for each rating.
    :type id: int

    :ivar movie_id: Identifier for the movie that the rating pertains to.
    :type movie_id: int

    :ivar user_id: Identifier for the user who made the rating.
    :type user_id: int

    :ivar rating: The numerical rating value given by the user for the movie.
    :type rating: float
    """

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """
        String representation of the Rating instance.

        :return: String representing the rating.
        :rtype: rating
        """
        return f"<Rating-{self.id}>"

    def save(self):
        """
        Save the current instance of Rating to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current instance of Rating from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def get_movie_id(self):
        """
        Get the movie ID of the current instance.

        :return: The ID of the movie that the rating pertains to.
        :rtype: int
        """
        return self.movie_id

    def get_movie_rating(self):
        """
        Get the rating value of the current instance.

        :return: The numerical rating value.
        :rtype: float
        """
        return self.rating

    def update_rating(self, new_rating):
        """
        Update the rating for the current instance.

        :param new_rating: The new rating value.
        :type new_rating: float
        """
        self.rating = new_rating
        db.session.commit()

    @staticmethod
    def create(movie_id, user_id, rating):
        """
        Create a new Rating instance, if it already exists then it will be updated.

        :param movie_id: Identifier for the movie that the rating pertains to.
        :type movie_id: int

        :param user_id: Identifier for the user who made the rating.
        :type user_id: int

        :param rating: The numerical rating value given by the user for the movie.
        :type rating: float

        :return: A new Rating instance or updated rating instance.
        :rtype: rating
        """
        rating_update = Rating.query.filter_by(movie_id=movie_id, user_id=user_id).first()
        if rating_update is not None:
            rating_update.update_rating(rating)

            return rating_update

        return Rating(movie_id=movie_id, user_id=user_id, rating=rating)
