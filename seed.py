from models import Type, db
from app import app

db.drop_all()
db.create_all()

hot_dogs = Type(name="Hot Dogs", freezer_months=2)
sausage = Type(name="Sausage", freezer_months=2)
raw_bacon = Type(name="Bacon, raw", freezer_months=2)
cooked_bacon = Type(name="Bacon, cooked", freezer_months=3)
cooked_ham = Type(name="Ham, cooked", freezer_months=4)
raw_ham = Type(name="Ham, raw", freezer_months=6)
fatty_fish = Type(name="Fatty Fish (ex. salmon, tuna), cooked or raw", freezer_months=3)
cooked_lean_fish = Type(name="Lean Fish (ex. cod, halibut), cooked", freezer_months=3)
raw_lean_fish = Type(name="Lean Fish (ex. cod, halibut), raw", freezer_months=8)
cooked_seafood = Type(name="Seafood (ex. crab, clams, shrimp), cooked", freezer_months=3)
raw_seafood = Type(name="Seafood (ex. crab, clams, NOT shrimp), raw", freezer_months=4)
raw_shrimp = Type(name="Shrimp, raw", freezer_months=6)
cooked_groud_meat = Type(name="Ground Meat, cooked", freezer_months=3)
raw_groud_meat = Type(name="Ground Meat, raw", freezer_months=4)
cooked_steaks_roasts = Type(name="Steaks/Roasts (beef, pork, lamb), cooked", freezer_months=3)
raw_steaks_roasts = Type(name="Steaks/Roasts (beef, pork, lamb), raw", freezer_months=12)
cooked_chicken = Type(name="Chicken, cooked", freezer_months=4)
raw_chicken = Type(name="Chicken, raw", freezer_months=12)

egg_whites = Type(name="Egg Whites", freezer_months=12)
fruits = Type(name="Most Fruit", freezer_months=12)
veggies = Type(name="Most Vegetables", freezer_months=12)
soup = Type(name="Soups/Stews/Broth, homemade or opened", freezer_months=6)

ice_cream = Type(name="Ice-Cream", freezer_months=4)
cookie_dough = Type(name="Cookie Dough", freezer_months=6)
baked_pie = Type(name="Pie, baked", freezer_months=8)
unbaked_pie = Type(name="Pie, unbaked", freezer_months=4)
bread = Type(name="Bread", freezer_months=3)
waffles = Type(name="Waffles/Pancakes", freezer_months=2)
pancake_mix = Type(name="Pancake/Waffle Mix", pantry_months=12)

cereal = Type(name="Most Cereals, opened", pantry_months=3)
oats = Type(name="Oats", pantry_months=24)
cooked_rice = Type(name="Rice (brown or white), cooked", freezer_months=6)
raw_brown_rice = Type(name="Brown Rice, uncooked", freezer_months=18, fridge_months=12, pantry_months=6)
white_rice = Type(name="White Rice, uncooked", pantry_months=-1)
beans = Type(name="Dried Beans/Lentils", pantry_months=36)
cooked_pasta = Type(name="Pasta, cooked", freezer_months=2)
dry_pasta = Type(name="Pasta, uncooked", pantry_months=36)
quinoa = Type(name="Quinoa", pantry_months=24)

whole_wheat_flour = Type(name="Whole Wheat Flour", freezer_months=12, fridge_months=8, pantry_months=3)
white_flour = Type(name="White Flour", freezer_months=24, fridge_months=24, pantry_months=12)
cornmeal = Type(name="Cornmeal", freezer_months=24, fridge_months=18, pantry_months=12)
baking_powder = Type(name="Baking Powder/Soda, opened", pantry_months=6)
tapioca_starch = Type(name="Tapioca Starch/Flour", pantry_months=24)

almonds = Type(name="Almonds", freezer_months=12, fridge_months=9, pantry_months=1)
peanuts = Type(name="Peanuts", freezer_months=12, fridge_months=6, pantry_months=1)
cashews = Type(name="Cashews", freezer_months=12, fridge_months=6, pantry_months=1)
sunflower_seeds = Type(name="Sunflower Seeds", freezer_months=12, fridge_months=12, pantry_months=3)
walnuts = Type(name="Walnuts", freezer_months=24, fridge_months=12, pantry_months=1)
pecans = Type(name="Pecans", freezer_months=24, fridge_months=9, pantry_months=1)
raisins = Type(name="Raisins", freezer_months=18, fridge_months=12, pantry_months=12)

avocado_oil = Type(name="Avocado Oil, opened", fridge_months=10, pantry_months=8)
canola_oil = Type(name="Canola/Vegetable Oil, opened", pantry_months=12)
olive_oil= Type(name="Olive Oil, opened", pantry_months=24)
cooking_spray = Type(name="Cooking Spray", pantry_months=24)
vinegars = Type(name="Many Vinegars: apple cider, red or white wine, rice", pantry_months=24)
balsamic_vinegar = Type(name="Balsamic Vinegar", pantry_months=36)
white_vinegar = Type(name="Distilled White Vinegar", pantry_months=-1)

herbs = Type(name="Most Dried Herbs (ex. oregano)", pantry_months=36)
spices = Type(name="Most Spices (ex. cinnamon, garlic powder)", pantry_months=48)
natural_peanut_butter = Type(name="Peanut Butter, natural, opened or not", fridge_months=6, pantry_months=1)
unnatural_peanut_butter = Type(name="Peanut Butter, w/stabilizers, opened", fridge_months=7, pantry_months=3)
jam = Type(name="Jams/Jellies, opened", fridge_months=12)
bread_crumbs = Type(name="Bread Crumbs", pantry_months=12)

pickles = Type(name="Pickles, opened", fridge_months=12)
relish = Type(name="Relish, opened", fridge_months=12)
ketchup = Type(name="Ketchup, opened", fridge_months=12)
mayo = Type(name="Mayonnaise, opened", fridge_months=12)
mustard = Type(name="Mustard, opened", fridge_months=18)
horseradish = Type(name="Horseradish, opened", fridge_months=4)
tartar_sauce = Type(name="Tartar Sauce, opened", fridge_months=6)
salad_dressing = Type(name="Salad Dressing, opened", fridge_months=9)
barbecue_sauce = Type(name="Barbecue Sauce, opened", fridge_months=9)
cocktail_sauce = Type(name="Cocktail Sauce, opened", fridge_months=9)
worcestershire = Type(name="Worcestershire Sauce, opened", fridge_months=36)
hot_sauce = Type(name="Hot Sauce, opened", fridge_months=60, pantry_months=6)
miso = Type(name="Miso Paste, opened or not", fridge_months=18)
teriyaki = Type(name="Teriyaki Sauce, opened", fridge_months=12)
soy_sauce = Type(name="Soy Sauce, opened", fridge_months=24, pantry_months=6)
oyster_sauce = Type(name="Oyster Sauce, opened", fridge_months=24)
fish_sauce = Type(name="Fish Sauce, opened or not", pantry_months=36)
sesame_oil = Type(name="Sesame Oil, opened", fridge_months=12)

tomato_sauce = Type(name="Tomato Sauce, unopened", pantry_months=24)
cans = Type(name="Most Canned/Bottled Products (ex. tuna, beans, veggies, soup, NOT tomato sauce), unopened", pantry_months=60)


db.session.add_all([])
db.session.commit()