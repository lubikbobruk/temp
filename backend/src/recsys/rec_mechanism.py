from .spearman_mechanism import SpearmanMechanism


class RecMechanism:
    """
    Recommends books to a target user based on Spearman's rank correlation coefficients
    calculated between the target user and all other users.
    """

    def __init__(self, target_user, all_users):
        self.MIN_CORRELATION = 0.7
        self.MIN_RATING = 4.5
        self.MAX_RECOMMENDATIONS = 20
        self.MAX_NEIGHBORS = 5

        self.target_user = target_user
        self.all_users = all_users
        self.spearman_correlation_coefficients = self._calculate_spearman_correlation_coefficients()

    def get_spearman_correlation_coefficients(self):
        """
        :return: Dict[user_id, correlation_coefficient]
        """
        return self.spearman_correlation_coefficients

    def get_recommendations(self):
        """
        :return: List of dicts, each with:
                  - id: recommended book ID
                  - similar_user_id
                  - similar_user_rating
                  - similar_user_correlation
        """
        return self._calculate_recommended_books()

    def get_predicted_rating_for_book(self, book_id):
        """
        :param book_id: int
        :return: float, predicted rating for this book
        """
        return self._calculate_predicted_rating_for_book(book_id)

    def _calculate_spearman_correlation_coefficients(self):
        return {
            user.get_id(): SpearmanMechanism(self.target_user, user)
                                        .get_spearman_correlation_coefficient()
            for user in self.all_users
            if user != self.target_user
        }

    def _calculate_recommended_books(self):
        recommendations = []
        # sort users by descending correlation
        sorted_users = sorted(
            self.spearman_correlation_coefficients.items(),
            key=lambda x: x[1],
            reverse=True
        )
        target_rated = set(self.target_user.get_ratings().keys())
        added = set()

        for user_id, corr in sorted_users:
            if corr < self.MIN_CORRELATION:
                continue

            neighbor = self.target_user.get_neighbor(user_id)
            # sort that user’s ratings descending
            sorted_books = sorted(
                neighbor.get_ratings().items(),
                key=lambda x: x[1],
                reverse=True
            )

            for book_id, rating in sorted_books:
                if rating < self.MIN_RATING:
                    continue
                if book_id not in target_rated and book_id not in added:
                    recommendations.append({
                        "id": book_id,
                        "similar_user_id": user_id,
                        "similar_user_rating": rating,
                        "similar_user_correlation": corr
                    })
                    added.add(book_id)
                    if len(recommendations) >= self.MAX_RECOMMENDATIONS:
                        break
            if len(recommendations) >= self.MAX_RECOMMENDATIONS:
                break

        return recommendations

    def _calculate_predicted_rating_for_book(self, book_id):
        # take top-N neighbors by correlation
        top_neighbors = sorted(
            self.spearman_correlation_coefficients.items(),
            key=lambda x: x[1],
            reverse=True
        )[:self.MAX_NEIGHBORS]

        sum_num = 0
        sum_den = 0
        base = self.target_user.get_mean_rating()

        for user_id, corr in top_neighbors:
            if corr < self.MIN_CORRELATION:
                continue
            neighbor = self.target_user.get_neighbor(user_id)
            ratings = neighbor.get_ratings()
            if book_id in ratings:
                mean_n = neighbor.get_mean_rating()
                sum_num += (ratings[book_id] - mean_n) * corr
                sum_den += abs(corr)

        if sum_den == 0:
            return base

        pred = base + sum_num / sum_den
        # clamp to [1,5]
        return max(1.0, min(5.0, pred))
