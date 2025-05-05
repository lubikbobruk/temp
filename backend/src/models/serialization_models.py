from flask_restx import fields

def create_login_model(ns):
    return ns.model("Login", {
        "user_email":   fields.String(required=True, description="User email"),
        "user_password": fields.String(required=True, description="User password")
    })

def create_user_model(ns):
    # tiny inline model for rating preview
    rating_preview = ns.model("RatingPreview", {
        "book_id":     fields.Integer,
        "book_rating": fields.Float
    })
    return ns.model("User", {
        "id":           fields.Integer,
        "name":         fields.String,
        "surname":      fields.String,
        "email":        fields.String,
        "ratings":      fields.List(fields.Nested(rating_preview)),
        "access_token": fields.String
    })

def create_prediction_model(ns):
    return ns.model("Prediction", {
        "user_id":               fields.Integer,
        "user_predicted_rating": fields.Float
    })

def create_book_model(ns):
    return ns.model("Book", {
        "id":          fields.Integer,
        "title":       fields.String,
        "author":      fields.String,
        "publisher":   fields.String,
        "year":        fields.Integer,
        "description": fields.String,
        "rating":      fields.Float,
    })

def create_book_preview_model(ns):
    return ns.model("Preview", {
        "id":    fields.Integer,
        "title": fields.String,
        "author": fields.String,
    })

def create_book_recommendation_model(ns):
    return ns.model("Recommendation", {
        "id":                        fields.Integer,
        "title":                     fields.String,
        "author":                    fields.String,
        "similar_user_id":           fields.Integer,
        "similar_user_rating":       fields.Float,
        "similar_user_correlation":  fields.Float
    })

def create_rating_model(ns):
    return ns.model("Rating", {
        "user_id":    fields.Integer,
        "book_rating": fields.Float
    })
