from .spearman_mechanism import SpearmanMechanism


class RecMechanism:
    """
    This class recommends movies to a target user based on the Spearman's rank correlation coefficient
    calculated between the target user and all other users.

    :ivar target_user: The target user for whom the recommendations are made.
    :type target_user: user

    :ivar all_users: A list of all other users in the dataset.
    :type all_users: list[user]

    :ivar MIN_CORRELATION: The minimum correlation value. Only users with a Spearman's correlation value
                           not lower than this will be considered when making recommendations.
    :type MIN_CORRELATION: float

    :ivar MIN_RATING: The minimum movie rating. Only movies with a rating not lower than this will be
                      recommended to the target user.
    :type MIN_RATING: float

    :ivar MAX_RECOMMENDATIONS: The maximum number of movie recommendations to return.
    :type MAX_RECOMMENDATIONS: int

    :ivar MAX_NEIGHBORS: The maximum number of nearest neighbors to consider when calculating the predicted
                         rating for a movie.
    :type MAX_NEIGHBORS: int

    :ivar spearman_correlation_coefficients: A dictionary containing the Spearman's rank correlation
                                             coefficients for the target user and all other users.
                                             The key is the user ID and the value is the correlation coefficient.
    :type spearman_correlation_coefficients: dict[int, float]

    Usage:
    To get a list of recommended movies for a target user based on the Spearman's rank correlation coefficient,
    create an instance of the RecMechanism class by providing the target user and a list of all users as arguments.
    Then, call the get_recommendations() method to get the list of recommended movies.

    Example:
    target_user = User(...)
    all_users = [User(...), User(...), ...]
    rec_mechanism = RecMechanism(target_user, all_users)
    correlation_coefficients = rec_mechanism.get_spearman_correlation_coefficients()
    recommended_movies = rec_mechanism.get_recommended_movies()
    predicted_movie_rating = rec_mechanism.get_predicted_movie_rating(movie_id)
    """

    def __init__(self, target_user, all_users):
        """
        The recommendation mechanism constructor.

        :param target_user: The target user for whom the recommendations are made.
        :type target_user: user

        :param all_users: A list of all other users in the dataset.
        :type all_users: list[user]
        """
        self.MIN_CORRELATION = 0.7
        self.MIN_RATING = 4.5
        self.MAX_RECOMMENDATIONS = 20
        self.MAX_NEIGHBORS = 5

        self.target_user = target_user
        self.all_users = all_users

        self.spearman_correlation_coefficients = self._calculate_spearman_correlation_coefficients()

    def get_spearman_correlation_coefficients(self):
        """
        Getter for the Spearman's correlation coefficients dictionary (was calculated earlier).

        :return: A dict containing the Spearman's rank correlation coefficients for the target user and all other users,
                 key: user ID, value: correlation coefficient.
        :rtype: dict[int, float]
        """
        return self.spearman_correlation_coefficients

    def get_recommendations(self):
        """
        Getter for the recommended movies for the target user.

        :return: A list of recommended movie dicts for the target user. Contains the following keys:
                               - id (int): The recommended movie ID.
                               - similar_user_id (int): The ID of the user whose recommendation is.
                               - similar_user_rating (float): The movie rating of the chosen similar user.
                               - similar_user_correlation (float): The Spearman's correlation value between the
                                                                   target user and another chosen user.
        :rtype: list[dict[str, any]]
        """
        recommendations = self._calculate_recommended_movies()

        return recommendations

    def get_predicted_rating_for_movie(self, movie_id):
        """
        Getter of the predicted rating for a specific movie for the target user using the Spearman's
        rank correlation coefficients between the target user and the nearest MAX_NEIGHBORS neighbors.

        :param movie_id: The ID of the movie for which the predicted rating will be calculated.
        :type movie_id: int

        :return: The predicted rating for the movie.
        :rtype: float
        """
        predicted_rating = self._calculate_predicted_rating_for_movie(movie_id)

        return predicted_rating

    def _calculate_spearman_correlation_coefficients(self):
        """
        Calculates the Spearman's rank correlation coefficients for the target user and all other users.

        :return: A dictionary containing the Spearman's rank correlation coefficients for the
                 target user and all other users, key: user ID, value: correlation coefficient.
        :rtype: dict[int, float]
        """
        return {user.get_id(): SpearmanMechanism(self.target_user, user).get_spearman_correlation_coefficient()
                for user in self.all_users if user != self.target_user}

    def _calculate_recommended_movies(self):
        """
        Calculates movie recommendations for the target user based on the Spearman's rank correlation coefficient
        between the target user and all other users.

        This method sorts the Spearman correlation coefficients in descending order,
        then for each user, it sorts their movie ratings in descending order.
        It then adds the movie to the recommendation list if it was not rated by the target user
        and if its rating is 4.5 or more.
        The process continues until it reaches the maximum number of recommendations.

        :return: List of recommended movies for the target user. Contains the following keys:
                               - id (int): The recommended movie ID.
                               - similar_user_id (int): The ID of the user whose recommendation is.
                               - similar_user_rating (float): The movie rating of the chosen similar user.
                               - similar_user_correlation (float): The Spearman's correlation value between the target
                                                                   user and another chosen user.
        :rtype: list[dict[str, any]]
        """
        # A list to store the recommended movies.
        recommendations = []

        # Users sorted by their Spearman correlation coefficients in descending order.
        sorted_users = sorted(self.spearman_correlation_coefficients.items(), key=lambda x: x[1], reverse=True)

        # A set of movie IDs that the target user has rated.
        target_user_rated_movies = set(self.target_user.get_ratings().keys())

        # A set to store the added movie IDs.
        added_movies = set()

        for user_id, correlation in sorted_users:
            # Only consider users with correlation not lower than MIN_CORRELATION.
            if correlation < self.MIN_CORRELATION:
                continue

            # The current user from the sorted list of users.
            user = self.target_user.get_neighbor(user_id)

            # The current user's movie ratings sorted in descending order.
            sorted_movie_ratings = sorted(user.get_ratings().items(), key=lambda x: x[1], reverse=True)

            for movie_id, rating in sorted_movie_ratings:
                # Only consider movies with rating not lower than MIN_RATING.
                if rating < self.MIN_RATING:
                    continue

                if movie_id not in target_user_rated_movies and movie_id not in added_movies:
                    # A dictionary containing movie ID, similar user ID, his movie rating, and correlation.
                    # Raw recommendation.
                    recommendation = {"id": movie_id, "similar_user_id": user_id,
                                      "similar_user_rating": rating, "similar_user_correlation": correlation}
                    recommendations.append(recommendation)
                    added_movies.add(movie_id)

                    if len(recommendations) >= self.MAX_RECOMMENDATIONS:
                        break

            if len(recommendations) >= self.MAX_RECOMMENDATIONS:
                break

        return recommendations

    def _calculate_predicted_rating_for_movie(self, movie_id):
        """
        Calculates the predicted rating for a specific movie for the target user using Spearman's rank correlation
        coefficients between the target user and the nearest neighbors.
        Uses the following formula:
            P_U1(M) = mean(U1) + (Σ[(U_i - mean(U_i)) * r_s(U1, U_i)]) / Σ[|r_s(U1, U_i)|]
        where P_U1(M) is the predicted rating for movie M for user U1,
        U_i is a nearest neighbor of user U1,
        and r_s(U1, U_i) is the Spearman's rank correlation between U1 and U_i.

        :param movie_id: The ID of the movie for which the predicted rating will be calculated.
        :type movie_id: int

        :return: The predicted rating for the movie.
        :rtype: float
        """
        # Sorting correlation coefficients in descending order and taking top MAX_NEIGHBORS.
        sorted_correlations = sorted(self.spearman_correlation_coefficients.items(),
                                     key=lambda x: x[1], reverse=True)[:self.MAX_NEIGHBORS]
        sum_numerator = 0
        sum_denominator = 0
        target_user_mean_rating = self.target_user.get_mean_rating()

        for user_id, correlation in sorted_correlations:
            if correlation >= self.MIN_CORRELATION:
                user = self.target_user.get_neighbor(user_id)
                user_ratings = user.get_ratings()

                if movie_id in user_ratings:
                    user_mean_rating = user.get_mean_rating()
                    sum_numerator += (user_ratings[movie_id] - user_mean_rating) * correlation
                    sum_denominator += abs(correlation)

        # If all correlation coefficients are below MIN_CORRELATION or the nearest neighbors haven't rated the movie.
        if sum_denominator == 0:
            return target_user_mean_rating
        else:
            predicted_rating = (target_user_mean_rating + sum_numerator / sum_denominator)
            if predicted_rating < 1:
                predicted_rating = 1
            if predicted_rating > 5:
                predicted_rating = 5
            return predicted_rating
