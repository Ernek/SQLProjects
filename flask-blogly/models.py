from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

# MODELS FOR BLOGLY
class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False, unique=False)
    last_name = db.Column(db.Text, nullable=False, unique=False)
    img_url = db.Column(db.Text, nullable = False, default=DEFAULT_IMAGE_URL)


def connect_db(app):
    db.app = app
    db.init_app(app)