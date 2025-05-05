class SpearmanMechanism:
    """
    Calculates Spearman's rank correlation coefficient between two users
    based on their book ratings.
    """

    def __init__(self, target_user, another_user):
        self.target_user = target_user
        self.another_user = another_user

        # IDs of books both users have rated
        self.common_books = self._get_common_rated_books()

        # rank maps: {book_id: rank}
        self.target_ranks = self._get_book_ranks(self.target_user, self.common_books)
        self.another_ranks = self._get_book_ranks(self.another_user, self.common_books)

        # sum of squared rank-differences
        self.squared_diffs = self._get_squared_rank_diffs_sum(
            self.common_books, self.target_ranks, self.another_ranks
        )

        # final coefficient
        self.coefficient = self._calculate_spearman(
            self.squared_diffs, len(self.common_books)
        )

    def get_spearman_correlation_coefficient(self):
        return self.coefficient

    @staticmethod
    def _get_common_rated_books():
        t = set(SpearmanMechanism.target_user.get_ratings().keys())
        a = set(SpearmanMechanism.another_user.get_ratings().keys())
        return list(t & a)

    @staticmethod
    def _get_book_ranks(user, common_books):
        # filter only those books
        ratings = {
            bid: r for bid, r in user.get_ratings().items()
            if bid in common_books
        }
        # sort by rating
        sorted_items = sorted(ratings.items(), key=lambda x: x[1])
        ranks = {}
        i = 0
        while i < len(sorted_items):
            val = sorted_items[i][1]
            # find ties
            count = 1
            for j in range(i+1, len(sorted_items)):
                if sorted_items[j][1] == val:
                    count += 1
                else:
                    break
            # average rank for ties
            avg_rank = sum(range(i+1, i+count+1)) / count
            for k in range(i, i+count):
                ranks[sorted_items[k][0]] = avg_rank
            i += count
        return ranks

    @staticmethod
    def _get_squared_rank_diffs_sum(common_books, ranks1, ranks2):
        return sum(
            (ranks1[b] - ranks2[b])**2 for b in common_books
        )

    @staticmethod
    def _calculate_spearman(sq_diff_sum, n):
        if n <= 1:
            # no variability
            return 0 if n == 0 else (1 if sq_diff_sum == 0 else 0)
        return 1 - (6 * sq_diff_sum) / (n * (n**2 - 1))
