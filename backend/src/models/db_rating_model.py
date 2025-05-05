from exts import db

class Rating(db.Model):
    __tablename__ = 'rating'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Rating id={self.id} book={self.book_id} val={self.rating}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_book_id(self):
        return self.book_id

    def get_rating(self):
        return self.rating

    def update_rating(self, new_rating):
        self.rating = new_rating
        db.session.commit()

    @staticmethod
    def create(book_id, user_id, rating):
        existing = Rating.query.filter_by(book_id=book_id, user_id=user_id).first()
        if existing:
            existing.update_rating(rating)
            return existing
        return Rating(book_id=book_id, user_id=user_id, rating=rating)
