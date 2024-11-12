from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "users"

    username = db.Column(
        db.String(15),
        primary_key=True
    )

    email = db.Column(
        db.String(),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(25),
        nullable=False
    )

    ingredients = db.relationship("Ingredient", backref="user")


class Ingredient(db.Model):
    """A user's ingredient"""

    __tablename__ = "ingredients"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(20),
        nullable=False
    )

    still_tasty_code  = db.Column(
        db.String(5),
        nullable=True
    )

    best_by_date = db.Column(
        db.Date,
        nullable=False,
        default=datetime.datetime(year=2500, month=12, day=30).date()
    )

    username = db.Column(
        db.String(15),
        db.ForeignKey("users.username"),
        nullable=False
    )

