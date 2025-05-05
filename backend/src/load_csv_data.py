import csv
import sys
import os

from main import create_app
from exts.config import DevConfig
from exts       import db
from models.db_book_model   import Book
from models.db_user_model   import User
from models.db_rating_model import Rating

# bootstrap your Flask app with the DevConfig
app = create_app(DevConfig)

def load_books(filepath):
    with app.app_context():
        with open(filepath, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                b = Book(
                    id=int(row['book_id']),
                    title=row['title'],
                    author=row['author'],
                    publisher=row.get('publisher',''),
                    year=int(row.get('year',0)),
                    description=row.get('description','')
                )
                db.session.add(b)
            db.session.commit()

def load_ratings(filepath):
    with app.app_context():
        with open(filepath, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                uid = int(row['user_id'])
                user = User.query.get(uid) or User(
                    id=uid,
                    name="User",
                    surname=str(uid),
                    email=f"{uid}@test.com",
                    password="1234"
                )
                db.session.add(user)
                db.session.flush()

                r = Rating(
                    user_id=uid,
                    book_id=int(row['book_id']),
                    rating=float(row['rating'])
                )
                db.session.add(r)
            db.session.commit()

if __name__ == "__main__":
    # pass in your CSV paths on the command line
    import sys
    books_csv  = sys.argv[1]
    ratings_csv= sys.argv[2]
    load_books(books_csv)
    load_ratings(ratings_csv)
    print("✅ Done loading data")
