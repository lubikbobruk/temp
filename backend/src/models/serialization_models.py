from flask_restx import fields


# Creates a login model for API endpoints.
def create_login_model(auth_namespace):
    return auth_namespace.model(
        "Login", {
            "user_email": fields.String(),
            "user_password": fields.String()
        }
    )


# Creates a user model for API endpoints.
def create_user_model(user_namespace):
    return user_namespace.model(
        "User", {
            "id": fields.Integer(),
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "ratings": fields.List(fields.Raw()),
            "access_token": fields.String()
        }
    )


# Creates a movie rating prediction model for API endpoints.
def create_prediction_model(user_namespace):
    return user_namespace.model(
        "Prediction", {
            "user_id": fields.Integer(),
            "user_predicted_rating": fields.String()
        }
    )


# Creates a movie model for API endpoints.
def create_movie_model(movies_namespace):
    return movies_namespace.model(
        "Movie", {
            "id": fields.Integer(),
            "title": fields.String(),
            "category": fields.String(),
            "country": fields.String(),
            "year": fields.Integer(),
            "main_actors": fields.String(),
            "description": fields.String(),
            "rating": fields.Float(),
            "comments": fields.List(fields.Raw())
        }
    )


# Creates a movie preview model for API endpoints.
def create_preview_model(movies_namespace):
    return movies_namespace.model(
        "Preview", {
            "id": fields.Integer(),
            "title": fields.String(),
            "category": fields.String(),
        }
    )


# Creates a movie preview recommendation model for API endpoints.
def create_recommendation_model(movies_namespace):
    return movies_namespace.model(
        "Recommendation", {
            "id": fields.Integer(),
            "title": fields.String(),
            "category": fields.String(),
            "similar_user_id": fields.Integer(),
            "similar_user_rating": fields.Float(),
            "similar_user_correlation": fields.Float()
        }
    )


# Creates a rating model for API endpoints.
def create_rating_model(movies_namespace):
    return movies_namespace.model(
        "Rating", {
            "user_id": fields.Integer(),
            "user_rating": fields.Float()
        }
    )


# Creates a comment model for API endpoints.
def create_comment_model(movies_namespace):
    return movies_namespace.model(
        "Comment", {
            "user_id": fields.Integer(),
            "user_comment": fields.String()
        }
    )
