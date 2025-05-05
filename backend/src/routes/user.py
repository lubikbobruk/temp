from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

from models.serialization_models import (
    create_user_model,
    create_book_recommendation_model as create_recommendation_model,
    create_prediction_model,
)
from controllers.user import UserController

user_namespace = Namespace("user", description="User related operations.")

user_model           = create_user_model(user_namespace)
recommendation_model = create_recommendation_model(user_namespace)
prediction_model     = create_prediction_model(user_namespace)


@user_namespace.route('/<int:id>')
class UserRouter(Resource):
    @user_namespace.response(404, "User not found")
    @user_namespace.marshal_with(user_model)
    @jwt_required()
    def get(self, id):
        """
        GET /user/<id>
        Return user data (including their ratings).
        """
        ctrl = UserController(id)
        data = ctrl.get_data()
        if data is None:
            return {"message": "User not found"}, 404
        return data, 200


@user_namespace.route('/<int:id>/recommendations')
class UserRecsRouter(Resource):
    @user_namespace.response(404, "User not found")
    @user_namespace.marshal_list_with(recommendation_model)
    @jwt_required()
    def get(self, id):
        """
        GET /user/<id>/recommendations
        Return a list of recommended books for this user.
        """
        ctrl = UserController(id)
        recs = ctrl.get_recommendations()
        if recs is None:
            return {"message": "User not found"}, 404
        return recs, 200


@user_namespace.route('/<int:id>/prediction/<int:book_id>')
class UserPredictionRouter(Resource):
    @user_namespace.response(404, "User or book not found")
    @user_namespace.marshal_with(prediction_model)
    @jwt_required()
    def get(self, id, book_id):
        """
        GET /user/<id>/prediction/<book_id>
        Return predicted rating for this user & book.
        """
        ctrl = UserController(id)
        pred = ctrl.get_predicted_book_rating(book_id)
        if pred is None:
            return {"message": "User or book not found"}, 404
        return pred, 200
