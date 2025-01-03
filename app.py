import os
import datetime

from flask import Flask, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, UserIngredient, Ingredient

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///ingredients'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


debug = DebugToolbarExtension(app)

connect_db(app)

@app.post("/api/users/add")
def add_user():
    """Add a new user"""

    username = request.json["username"]
    password = request.json["password"]    #TODO: Proper passwording
    email = request.json["email"]

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify(f"New user {username} added")     #TODO: Errors

@app.delete("/api/users/<username>/delete")
def delete_user(username):
    """Delete a user"""

    user = User.query.get_or_404(username)

    db.session.delete(user)
    db.session.commit()

    return jsonify(f"User {username} deleted")

@app.get("/api/ingredients/<int:id>/months")
def get_best_months(id):
    """Get the ideal shelf life in months of an ingredient for all recommended
    storage methods
    Ex: {
        "name": "Peanut Butter",
        "shelf_life": {
            "pantry": 3,
            "fridge": 7
        }
    }
    """

    ingredient = Ingredient.query.get_or_404(id)

    out = {}

    out["name"] = ingredient.name
    out["shelf_life"] = {}

    if (ingredient.pantry_months is not None):
        out["shelf_life"]["pantry"] = ingredient.pantry_months

    if (ingredient.fridge_months is not None):
        out["shelf_life"]["fridge"] = ingredient.fridge_months

    if (ingredient.freezer_months is not None):
        out["shelf_life"]["freezer"] = ingredient.freezer_months

    return jsonify(out)


@app.post("/api/users/<username>/add_ingredient")
def add_ingredient(username):
    """Add a new ingredient to a user's list"""

    name = request.json["name"]
    meals_worth = request.json.get("meals_worth", 5)
    high_value = request.json.get("high_value", False)
    storage_method = request.json["storage_method"]
    purchase_date = request.json.get("purchase_date", datetime.date.today())
    best_by_date = request.json.get("best_by_date", "2500-12-30")
    ingredient_id = request.json.get("ingredient_id")
    suggest = request.json.get("suggest", True)
    last_used = request.json.get("last_used", "2000-01-01")

    ingredient = UserIngredient(
        username=username,
        name=name,
        meals_worth = meals_worth,
        high_value = high_value,
        storage_method = storage_method,
        purchase_date=purchase_date,
        best_by_date=best_by_date,
        ingredient_id = ingredient_id,
        suggest=suggest,
        last_used=last_used
    )

    db.session.add(ingredient)
    db.session.commit()

    return jsonify(f"New {name} added")

@app.get("/api/users/<username>/get_ingredients")
def get_ingredients(username):
    """Retrieve all ingredients for a user, ordered by ingredient_id"""

    ingredients = (UserIngredient.query
                   .filter_by(username=username)
                   .order_by(
                       UserIngredient.ingredient_id.is_(None),
                       "ingredient_id",
                       "name",
                       "purchase_date"
                    )
                   .all())

    out = [ingredient.to_dict() for ingredient in ingredients]

    return jsonify(out)