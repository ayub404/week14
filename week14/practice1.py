pantry = ["Eggs", "flour", "Milk", "eggs", "salt"]
recipe = ["flour", "milk", "Sugar", "Eggs", "butter"]

def check_ingredients(pantry, recipe):

    pantry_se = [item.lower() for item in pantry]
    recipe_se = [item.lower() for item in recipe]
    pantry_set = set(pantry_se)
    recipe_set = set(recipe_se)
    missing = sorted(recipe_set - pantry_set)
    availabe = sorted(recipe_set & pantry_set)
    return missing, availabe

missing, available = check_ingredients(pantry, recipe)
print(f"Need to buy: {missing}")
print(f"Already have: {available}")
