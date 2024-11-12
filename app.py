import os

from flask import Flask, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, Ingredient
# TODO: Check order of boiler plate stuff in project that has all this

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///ingredients'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


debug = DebugToolbarExtension(app)

connect_db(app)

@app.post("/api/add_user")
def add_user():
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

@app.post("/api/add_ingredient")
def add_ingredient():
    username = request.json["username"]
    name = request.json["name"]

    ingredient = Ingredient(username=username, name=name)
    db.session.add(ingredient)
    db.session.commit()

@app.get("/api/get_ingredients")
def get_ingredient():
    username = request.json["username"]

    user = User.query.get(username)

    out = []
    for ingredient in user.ingredients:
        out.append(ingredient.name)

    return jsonify(out)

