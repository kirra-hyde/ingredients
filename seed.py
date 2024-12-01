from models import User, Ingredient, Type, db
from app import app

db.drop_all()
db.create_all()



