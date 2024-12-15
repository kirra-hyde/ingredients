from models import Ingredient, User, UserIngredient, db
from app import app

db.drop_all()
db.create_all()

hot_dogs = Ingredient(name="Hot Dogs", freezer_months=2)
sausage = Ingredient(name="Sausage, cooked or raw", freezer_months=2)
frozen_sausage = Ingredient(name="Sausage, cooked, purchased frozen", freezer_months=6)
cooked_bacon = Ingredient(name="Bacon, cooked", freezer_months=3)
raw_bacon = Ingredient(name="Bacon, raw", freezer_months=2)
cooked_ham = Ingredient(name="Ham, cooked", freezer_months=4)
raw_ham = Ingredient(name="Ham, raw", freezer_months=6)

fatty_fish = Ingredient(name="Fatty Fish (ex. salmon, tuna), cooked or raw", freezer_months=3)
frozen_fatty_fish = Ingredient(name="Fatty Fish (ex. salmon, tuna), raw, purchased frozen", freezer_months=9)
cooked_lean_fish = Ingredient(name="Lean Fish (ex. cod, halibut), cooked", freezer_months=3)
raw_lean_fish = Ingredient(name="Lean Fish (ex. cod, halibut), raw", freezer_months=8)
frozen_lean_fish = Ingredient(name="Lean Fish (ex. cod, halibut), raw, purchased frozen", freezer_months=12)
cooked_shellfish = Ingredient(name="Shellfish (all sorts), cooked", freezer_months=3)
raw_shrimp = Ingredient(name="Shrimp, raw", freezer_months=6)
frozen_shrimp = Ingredient(name="Shrimp, raw, purchased frozen", freezer_months=9)
raw_bivalve = Ingredient(name="Bivalves (ex. clams, mussels), raw", freezer_months=4)
frozen_bivalve = Ingredient(name="Bivalves (ex. clams, mussels), raw, purchased frozen", freezer_months=12)

cooked_ground_meat = Ingredient(name="Ground Meat, cooked", freezer_months=3)
raw_ground_meat = Ingredient(name="Ground Meat, raw", freezer_months=4)
cooked_steaks_roasts = Ingredient(name="Steaks/Roasts (beef, pork, lamb), cooked", freezer_months=3)
raw_steaks_roasts = Ingredient(name="Steaks/Roasts (beef, pork, lamb), raw", freezer_months=12)
cooked_chicken = Ingredient(name="Chicken, cooked", freezer_months=4)
raw_chicken = Ingredient(name="Chicken, raw", freezer_months=12)

egg_whites = Ingredient(name="Egg Whites", freezer_months=12)
fruits = Ingredient(name="Most Fruit, purchased frozen or not", freezer_months=12)
veggies = Ingredient(name="Most Vegetables, purchased frozen", freezer_months=12)
soup = Ingredient(name="Soups/Stews/Broth, homemade or opened", freezer_months=6)

ice_cream = Ingredient(name="Ice-Cream", freezer_months=4)
cookie_dough = Ingredient(name="Cookie Dough, homemade", freezer_months=6)
fridge_cookie_dough = Ingredient(name="Cookie Dough, store bought from fridge section", freezer_months=4)
bread = Ingredient(name="Bread", freezer_months=3)
waffles = Ingredient(name="Waffles/Pancakes", freezer_months=2)
frozen_waffles = Ingredient(name="Waffles, purchased frozen", freezer_months=4)
pancake_mix = Ingredient(name="Pancake/Waffle Mix", pantry_months=12)

cereal = Ingredient(name="Most Cereals, opened", pantry_months=3)
closed_cereal = Ingredient(name="Most Cereals, unopened", pantry_months=12)
oats = Ingredient(name="Oats", pantry_months=24)
cooked_rice = Ingredient(name="Rice (brown or white), cooked", freezer_months=6)
raw_brown_rice = Ingredient(name="Brown Rice, uncooked", freezer_months=18, fridge_months=12, pantry_months=6)
white_rice = Ingredient(name="White Rice, uncooked", pantry_months=-1)
beans = Ingredient(name="Dried Beans/Lentils", pantry_months=36)
cooked_pasta = Ingredient(name="Pasta, cooked", freezer_months=2)
dry_pasta = Ingredient(name="Dry Pasta, uncooked", pantry_months=36)
quinoa = Ingredient(name="Quinoa, uncooked", pantry_months=24)

whole_wheat_flour = Ingredient(name="Whole Wheat Flour", freezer_months=12, fridge_months=8, pantry_months=3)
white_flour = Ingredient(name="White Flour", freezer_months=24, fridge_months=24, pantry_months=12)
cornmeal = Ingredient(name="Cornmeal, regular", freezer_months=24, fridge_months=18, pantry_months=12)
baking_powder = Ingredient(name="Baking Powder/Soda, opened", pantry_months=6)
tapioca_starch = Ingredient(name="Tapioca Starch/Flour", pantry_months=24)

almonds = Ingredient(name="Almonds, bagged", freezer_months=12, fridge_months=9, pantry_months=1)
bottled_almonds = Ingredient(name="Almonds, opened bottle", freezer_months=12, fridge_months=6, pantry_months=1)
peanuts = Ingredient(name="Peanuts, bagged or opened bottle", freezer_months=12, fridge_months=6, pantry_months=1)
cashews = Ingredient(name="Cashews, bagged or opened bottle", freezer_months=12, fridge_months=6, pantry_months=1)
walnuts = Ingredient(name="Walnuts, bagged", freezer_months=24, fridge_months=12, pantry_months=1)
pecans = Ingredient(name="Pecans, bagged", freezer_months=24, fridge_months=9, pantry_months=1)
sunflower_seeds = Ingredient(name="Sunflower Seeds", freezer_months=12, fridge_months=12, pantry_months=3)
raisins = Ingredient(name="Raisins/Dried Fruits", freezer_months=18, fridge_months=12, pantry_months=12)

avocado_oil = Ingredient(name="Avocado Oil, opened", fridge_months=12, pantry_months=8)
canola_oil = Ingredient(name="Canola/Vegetable Oil, opened", pantry_months=12)
olive_oil= Ingredient(name="Olive Oil, opened", pantry_months=24)
cooking_spray = Ingredient(name="Cooking Spray", pantry_months=24)
vinegars = Ingredient(name="Many Vinegars: apple cider, red or white wine, rice", pantry_months=24)
balsamic_vinegar = Ingredient(name="Balsamic Vinegar", pantry_months=36)
white_vinegar = Ingredient(name="Distilled White Vinegar", pantry_months=-1)

herbs = Ingredient(name="Most Dried Herbs (ex. oregano)", pantry_months=36)
spices = Ingredient(name="Most Spices (ex. cinnamon, garlic powder)", pantry_months=48)
nat_peanut_butter = Ingredient(name="Peanut Butter, natural, opened or not", fridge_months=6, pantry_months=1)
unnatural_peanut_butter = Ingredient(name="Peanut Butter, w/stabilizers, opened", fridge_months=7, pantry_months=3)
jam = Ingredient(name="Jams/Jellies, opened", fridge_months=12)
bread_crumbs = Ingredient(name="Bread Crumbs", pantry_months=12)

pickles = Ingredient(name="Pickles, opened", fridge_months=12)
relish = Ingredient(name="Relish, opened", fridge_months=12)
ketchup = Ingredient(name="Ketchup, opened", fridge_months=12)
mayo = Ingredient(name="Mayonnaise, opened", fridge_months=12)
mustard = Ingredient(name="Mustard (all types), opened", fridge_months=18)
horseradish = Ingredient(name="Horseradish, opened", fridge_months=4)
tartar_sauce = Ingredient(name="Tartar Sauce, opened", fridge_months=6)
salad_dressing = Ingredient(name="Most Salad Dressings, opened", fridge_months=9)
barbecue_sauce = Ingredient(name="Barbecue Sauce, opened", fridge_months=9)
cocktail_sauce = Ingredient(name="Cocktail Sauce, opened", fridge_months=9)
worcestershire = Ingredient(name="Worcestershire Sauce, opened", fridge_months=36)
hot_sauce = Ingredient(name="Hot Sauce, opened", fridge_months=60, pantry_months=6)
miso = Ingredient(name="Miso Paste, opened or not", fridge_months=18)
teriyaki = Ingredient(name="Teriyaki Sauce, opened", fridge_months=12)
soy_sauce = Ingredient(name="Soy Sauce, opened", fridge_months=24, pantry_months=6)
oyster_sauce = Ingredient(name="Oyster Sauce, opened", fridge_months=24)
fish_sauce = Ingredient(name="Fish Sauce, opened or not", pantry_months=36)
sesame_oil = Ingredient(name="Sesame Oil, opened", fridge_months=12)

tomato_sauce = Ingredient(name="Tomato Sauce, unopened", pantry_months=24)
cans = Ingredient(name="Most Canned/Bottled Products (NOT tomato sauce), unopened", pantry_months=60)


db.session.add_all([
    hot_dogs, sausage, frozen_sausage, cooked_bacon, raw_bacon, cooked_ham,
    raw_ham, fatty_fish, frozen_fatty_fish, cooked_lean_fish, raw_lean_fish,
    frozen_lean_fish, cooked_shellfish, raw_shrimp, frozen_shrimp, raw_bivalve,
    frozen_bivalve, cooked_ground_meat, raw_ground_meat, cooked_steaks_roasts,
    raw_steaks_roasts, cooked_chicken, raw_chicken, egg_whites, fruits, veggies,
    soup, ice_cream, cookie_dough, fridge_cookie_dough, bread, waffles,
    frozen_waffles, pancake_mix, cereal, closed_cereal, oats, cooked_rice,
    raw_brown_rice, white_rice, beans, cooked_pasta, dry_pasta, quinoa,
    whole_wheat_flour, white_flour, cornmeal, baking_powder, tapioca_starch,
    almonds, bottled_almonds, peanuts, cashews, walnuts, pecans, sunflower_seeds,
    raisins, avocado_oil, canola_oil, olive_oil, cooking_spray, vinegars,
    balsamic_vinegar, white_vinegar, herbs, spices, nat_peanut_butter,
    unnatural_peanut_butter, jam, bread_crumbs, pickles, relish, ketchup, mayo,
    mustard, horseradish, tartar_sauce, salad_dressing, barbecue_sauce,
    cocktail_sauce, worcestershire, hot_sauce, miso, teriyaki, soy_sauce,
    oyster_sauce, fish_sauce, sesame_oil, tomato_sauce, cans
])
db.session.commit()