from ..models import Movie


class MoviesController:
    """
    MoviesController class for handling movies-related operations.
    """

    @staticmethod
    def get_movies():
        """
        Retrieve all movie data.

        :return: A list of dictionaries containing movie previews:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
        :rtype: list[dict[str, any]]
        """
        return Movie.get_all()

    @staticmethod
    def validate_sort_parameters(params):
        """
        Validate the provided sort parameters.

        :param params: The parameters for sorting movies.
        :type params: dict

        :return: True if parameters are valid, False otherwise.
        :rtype: bool
        """
        return Movie.validate_sort_parameters(params)

    @staticmethod
    def get_movies_sorted(params):
        """
        Retrieve sorted movie data based on the provided parameters.

        :param params: The parameters for sorting movies.
        :type params: dict

        :return: A list of dictionaries containing sorted movie previews:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
        :rtype: list[dict[str, any]]
        """
        return Movie.sort_all(params)
