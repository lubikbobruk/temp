from exts import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(60), nullable=False)
    publisher = db.Column(db.String(60), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)

    # one‐to‐many: ratings for this book
    ratings = db.relationship("Rating", backref="book", lazy='dynamic')

    def __repr__(self):
        return f"<Book id={self.id} title={self.title!r}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def _get_rating(self):
        all_r = self.ratings.all()  # if you use lazy='dynamic'
        if not all_r:
            return 0
        return sum(r.rating for r in all_r) / len(all_r)

    def get_data(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "year": self.year,
            "description": self.description,
            "rating": self._get_rating(),
        }

    @staticmethod
    def get_all():
        return [book.get_data() for book in Book.query.all()]

    @staticmethod
    def get_by_id(book_id):
        return Book.query.get(book_id)
