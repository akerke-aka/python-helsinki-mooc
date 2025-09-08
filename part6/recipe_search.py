"""
Recipe search
-------------
This code allows reading recipes from a file and search them by name, preparation time or ingredients.

Functions:
- read_file(filename): reads recipe data from a file and returns a list of recipes
- search_by_name(filename, word): returns recipe names whose name contain the given word
- search_by_time(filename, prep_time): returns recipe names with preparation time less than or equal to given time
- search_by_ingredient(filename, ingredient): returns recipe names that contain a given ingredient
"""
def read_file(filename):
    recipe_list = []
    with open(filename) as new_file:
        recipe= []
        for line in new_file:
            line = line.strip()
            if line != "":
                # add recipe data (line)  to current recipe
                recipe.append(line)
            else:
                # end of one recipe, add to list and reset
                recipe_list.append(recipe)
                recipe = []
        if recipe:
            recipe_list.append(recipe) # add last recipe if file didn't end with a blank line
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
        if ingredient in recipe[1:]: #ingredients start from index 1
            found.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found
