from flask_jwt_extended import create_access_token
from exts import db
from recsys import RecMechanism

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    ratings = db.relationship("Rating", backref="user", lazy='dynamic')

    def __repr__(self):
        return f"<User id={self.id} email={self.email!r}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_data(self):
        all_r = self.ratings.all()
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "ratings": [
                {"book_id": r.get_book_id(), "book_rating": r.get_rating()}
                for r in all_r
            ]
        }

    def get_login_data(self):
        data = self.get_data()
        data["access_token"] = create_access_token(identity=self.email)
        return data

    def get_recommendations(self):
        return RecMechanism(self, User.get_all()).get_recommendations()

    def get_predicted_rating(self, book_id):
        return {
            "user_id": self.id,
            "user_predicted_rating": RecMechanism(self, User.get_all()).get_predicted_rating_for_book(book_id)
        }

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()
