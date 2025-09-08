def read_file(filename):
    recipe_list = []
    with open(filename) as new_file:
        recipe= []
        for line in new_file:
            line = line.strip()
            if line != "":
                recipe.append(line)
            else:
                recipe_list.append(recipe)
                recipe = []
        if recipe:
            recipe_list.append(recipe)
    return recipe_list

def search_by_name(filename: str, word: str):
    found = []
    recipes = read_file(filename)
    for recipe in recipes:
        name = recipe[0]
        if word.lower() in name.lower():
            found.append(name)
    return found

def search_by_time(filename: str, prep_time: int):
    found = []
    recipes = read_file(filename)
    for recipe in recipes:
        time = int(recipe[1])
        if time <= prep_time:
            found.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found

def search_by_ingredient(filename: str, ingredient: str):
    found = []
    recipes = read_file(filename)
    for recipe in recipes:
        if ingredient in recipe[1:]:
            found.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found