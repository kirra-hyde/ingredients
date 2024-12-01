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

    meals_worth = db.Column(
        db.Integer,
        nullable=False
    )

    high_value = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    storage_method = db.Column(
        db.String(7),
        db.CheckConstraint(
            "storage_method IN ('fridge', 'pantry', 'freezer')",
            name="check_valid_storage_method"
        ),
        nullable=False
    )

    ingredient_type = db.Column(
        db.Integer,
        db.ForeignKey("types.id"),
        nullable=True
    )


class Type(db.Model):
    """Types of ingredients"""

    __tablename__ = "types"

    __table_args__ = (
        db.CheckConstraint(
            """freezer_months IS NOT NULL OR
               fridge_months IS NOT NULL OR
               pantry_months IS NOT NULL""",
            name="check_for_a_non_null_storage_months"
        ),
    )

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    ingredients = db.relationship("Ingredient", backref="type")

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    freezer_months = db.Column(
        db.Integer,
        nullable=True
    )

    fridge_months = db.Column(
        db.Integer,
        nullable=True
    )

    pantry_months = db.Column(
        db.Integer,
        nullable=True
    )