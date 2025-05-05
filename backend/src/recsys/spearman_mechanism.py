class SpearmanMechanism:
    """
    A class for calculating Spearman's rank correlation coefficient between two users based on their movie ratings.

    :ivar target_user: A user object representing the primary target user.
    :type target_user: user

    :ivar another_user: A user object representing the secondary user.
    :type another_user: user

    :ivar target_user_rated_movie_ranks: A dictionary containing the ranked movie IDs and their ranks for
                                         the target user. Key: movie ID, Value: rank value.
    :type target_user_rated_movie_ranks: dict[int, float]

    :ivar another_user_rated_movie_ranks: A dictionary containing the ranked movies and their ranks for
                                          another user. Key: movie ID, Value: rank value.
    :type another_user_rated_movie_ranks: dict[int, float]

    :ivar common_rated_movies: A list of movie IDs that were rated by both users.
    :type common_rated_movies: list[int]

    :ivar squared_common_rated_movies_rank_diffs_sum: Sum of squared rank differences for common rated movies.
    :type squared_common_rated_movies_rank_diffs_sum: float

    :ivar spearman_correlation_coefficient: Spearman's rank correlation coefficient between the two users
                                            based on their movie ratings.
    :type spearman_correlation_coefficient: float

    Usage:
    To calculate the Spearman's rank correlation coefficient between two users based on their movie ratings,
    create an instance of the SpearmanMechanism class by providing two user objects as arguments.
    The class will calculate the required variables and the final correlation coefficient,
    which can be accessed via the getter get_spearman_correlation_coefficient().

    Example:
    user1 = User(...)
    user2 = User(...)
    spearman_mechanism = SpearmanMechanism(user1, user2)
    correlation_coefficient = spearman_mechanism.get_spearman_correlation_coefficient()
    """

    def __init__(self, target_user, another_user):
        """
        Initialize the SpearmanMechanism with two user objects.

        :param target_user: A user object representing the primary user.
        :type target_user: user

        :param another_user: A user object representing the secondary user.
        :type another_user: user
        """
        self.target_user = target_user
        self.another_user = another_user

        self.common_rated_movies = self._get_common_rated_movies(self.target_user, self.another_user)

        self.target_user_rated_movie_ranks = self._get_rated_movie_ranks(self.target_user, self.common_rated_movies)
        self.another_user_rated_movie_ranks = self._get_rated_movie_ranks(self.another_user, self.common_rated_movies)

        self.squared_common_rated_movies_rank_diffs_sum = \
            self._get_common_rated_movie_ranks_squared_diffs_sum(
                self.common_rated_movies, self.target_user_rated_movie_ranks, self.another_user_rated_movie_ranks
            )

        self.spearman_correlation_coefficient = self._calculate_spearman_correlation_coefficient(
            self.squared_common_rated_movies_rank_diffs_sum, len(self.common_rated_movies)
        )

    def get_spearman_correlation_coefficient(self):
        """
        Spearman's correlation coefficient getter (was calculated earlier).

        :return: The Spearman's rank correlation coefficient.
        :rtype: float
        """
        return self.spearman_correlation_coefficient

    @staticmethod
    def _get_rated_movie_ranks(user, common_rated_movies):
        """
        This method calculates and returns the ranks for movies commonly rated by a user.

        :param user: The user whose rated movies' ranks are to be calculated.
        :type user: user

        :param common_rated_movies: A list of movie IDs that are commonly rated between two users.
        :type common_rated_movies: list[int]

        :return: A dictionary where each key is a movie ID and its corresponding value is the rank value of that movie.
        :rtype: dict[int, float]
        """
        # Filter the user's ratings to include only the common rated movies.
        user_ratings = {movie_id: rating for movie_id, rating in user.get_ratings().items() if
                        movie_id in common_rated_movies}

        # A list of tuples where each tuple contains a movie ID and its corresponding rating.
        # The list is sorted by rating value.
        sorted_ratings = sorted(user_ratings.items(), key=lambda x: x[1])

        # A dictionary where each key is a movie ID and its corresponding value is the rank of that movie.
        ranks = {}

        i = 0
        while i < len(sorted_ratings):
            current_rating = sorted_ratings[i][1]

            # A variable that holds the count of movies with the same rating.
            same_ratings_count = 1

            for j in range(i + 1, len(sorted_ratings)):
                if sorted_ratings[j][1] == current_rating:
                    same_ratings_count += 1
                else:
                    break

            # A variable that holds the average value of rank based on the movies with the same rating.
            average_rank = sum(range(i + 1, i + same_ratings_count + 1)) / same_ratings_count

            for k in range(i, i + same_ratings_count):
                ranks[sorted_ratings[k][0]] = average_rank

            i += same_ratings_count

        return ranks

    @staticmethod
    def _get_common_rated_movies(target_user, another_user):
        """
        Retrieves the common movies that were rated by both the target user and another user.

        :param target_user: The first user for which we are finding common rated movies.
        :type target_user: user

        :param another_user: The second user for which we are finding common rated movies.
        :type another_user: user

        :return: A list of IDs representing common movies rated by both the target user and another user.
        :rtype: list[int]
        """
        # A set of IDs corresponding to movies rated by our target user.
        target_user_movie_ids = set(target_user.get_ratings().keys())

        # A set of IDs corresponding to movies rated by another user.
        another_user_movie_ids = set(another_user.get_ratings().keys())

        # A set of IDs corresponding to common movies that were rated by both the target user and another user.
        common_movie_ids = target_user_movie_ids & another_user_movie_ids

        return list(common_movie_ids)

    @staticmethod
    def _get_common_rated_movie_ranks_squared_diffs_sum(common_rated_movies,
                                                        target_user_rated_movie_ranks, another_user_rated_movie_ranks):
        """
        Calculates the sum of squared differences in ranks of common rated movies between two users.

        :param common_rated_movies: A list of IDs of common rated movies.
        :type common_rated_movies: list[int]

        :param target_user_rated_movie_ranks: A dictionary where each key is a movie ID and its corresponding value
                                              is the rank of that movie for the target user.
        :type target_user_rated_movie_ranks: dict[int, float]

        :param another_user_rated_movie_ranks: A dictionary where each key is a movie ID and its corresponding value
                                               is the rank of that movie for another user.
        :type another_user_rated_movie_ranks: dict[int, float]

        :return: The sum of squared differences in ranks of common rated movies between the two users.
        :rtype: float
        """
        squared_rank_diffs_sum = sum(
            (target_user_rated_movie_ranks[movie_id] - another_user_rated_movie_ranks[movie_id]) ** 2
            for movie_id in common_rated_movies
        )

        return squared_rank_diffs_sum

    @staticmethod
    def _calculate_spearman_correlation_coefficient(squared_rank_diffs_sum, common_rated_movies_count):
        """
        This method calculates Spearman's rank correlation coefficient based on the sum of squared rank differences and
        the count of common rated movies. It implements the formula:

        ρ = 1 - [ (6 * Σdᵢ²) / (n * (n² - 1)) ],

        where:

        - Σdᵢ² represents the sum of the squares of the rank differences of the commonly rated movies between two users.
        - n is the number of commonly rated movies.

        In this formula, each commonly rated movie between two users is represented by a pair of ranks (rᵢ, sᵢ), where
        rᵢ is the rank of the movie for the target user and sᵢ is the rank of the movie for the other user.
        "dᵢ" in this context represents the difference between the ranks: dᵢ = rᵢ - sᵢ.

        This formula measures the degree of monotonic association between the movie ranks of the two users.
        If the movie ranks are identical for both users, the Spearman correlation coefficient will be 1.
        If the movie ranks for one user are the precise reverse of the ranks for the other user (i.e., one user ranks
        movies in the reverse order of the other), the Spearman correlation coefficient will be -1.
        If there is no association between the ranks, the Spearman coefficient will be near zero.

        :param squared_rank_diffs_sum: The sum of squared differences in ranks of common rated movies.
        :type squared_rank_diffs_sum: float

        :param common_rated_movies_count: The count of common rated movies.
        :type common_rated_movies_count: int

        :return: Spearman's rank correlation coefficient.
        :rtype: float
        """
        if common_rated_movies_count <= 1:
            return 0 if common_rated_movies_count == 0 else (1 if squared_rank_diffs_sum == 0 else 0)

        numerator = 6 * squared_rank_diffs_sum
        denominator = common_rated_movies_count * (common_rated_movies_count ** 2 - 1)
        spearman_correlation_coefficient = 1 - (numerator / denominator)

        return spearman_correlation_coefficient
