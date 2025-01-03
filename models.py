from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Users"""

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

    ingredients = db.relationship(
        "UserIngredient",
        cascade="all, delete-orphan",
        backref="user"
    )


class UserIngredient(db.Model):
    """A user's ingredients"""

    __tablename__ = "user_ingredients"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False
    )

    purchase_date = db.Column(
        db.Date,
        nullable=False,
        default=datetime.date.today()
    )

    best_by_date = db.Column(
        db.Date,
        nullable=False,
        default=datetime.datetime(year=2500, month=12, day=30).date()
    )

    meals_worth = db.Column(
        db.Integer,
        nullable=False,
        default=5
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

    suggest = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    last_used = db.Column(
        db.Date,
        nullable=False,
        default=datetime.datetime(year=2000, month=1, day=1).date()
    )

    ingredient_id = db.Column(
        db.Integer,
        db.ForeignKey("ingredients.id"),
        nullable=True
    )

    username = db.Column(
        db.String(15),
        db.ForeignKey("users.username"),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "purchase_date": self.purchase_date.isoformat(),
            "best_by_date": self.best_by_date.isoformat(),
            "username": self.username,
            "meals_worth": self.meals_worth,
            "high_value": self.high_value,
            "storage_method": self.storage_method,
            "ingredient_id": self.ingredient_id,
            "suggest": self.suggest,
            "last_used": self.last_used.isoformat()
        }


class Ingredient(db.Model):
    """Ingredients"""

    __tablename__ = "ingredients"

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

    name = db.Column(
        db.String(65),
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

    user_ingredients = db.relationship(
        "UserIngredient",
        backref="ingredient_type"
    )