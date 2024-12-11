import os

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

    if (ingredient.pantry_months != None):
        out["shelf_life"]["pantry"] = ingredient.pantry_months

    if (ingredient.fridge_months != None):
        out["shelf_life"]["fridge"] = ingredient.fridge_months

    if (ingredient.freezer_months != None):
        out["shelf_life"]["freezer"] = ingredient.freezer_months

    return jsonify(out)


@app.post("/api/users/<username>/add_ingredient")
def add_ingredient(username):
    name = request.json["name"]
    meals_worth = request.json["meals_worth"]
    high_value = request.json["high_value"]
    storage_method = request.json["storage_method"]

    ingredient = UserIngredient(
        username=username,
        name=name,
        meals_worth = meals_worth,
        high_value = high_value,
        storage_method = storage_method
    )

    db.session.add(ingredient)
    db.session.commit()

    return jsonify(f"New {name} added")

@app.get("/api/users/<username>/get_ingredients")
def get_ingredient(username):

    user = User.query.get(username)

    out = []
    for ingredient in user.ingredients:
        out.append(ingredient.name)

    return jsonify(out)

