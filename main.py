"""LU02 a08"""
import json


# Dein Code kommt hier hin
def adjust_recipe(recipe, amount_of_people):
    new_ingredients = {}
    for ingredient, amount in recipe['ingredients'].items():
        new_ingredients[ingredient] = amount / recipe['servings'] * amount_of_people
        print(ingredient, amount)

    new_recipe = {
        'title': recipe['title'],
        'ingredients': new_ingredients,
        'servings': amount_of_people
    }

    print(new_recipe)

    return new_recipe


def load_recipe(json_string):
    return json.loads(json_string)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    # Dein Code kommt hier hin
    recipe_dict = load_recipe(recipe_json)
    adjust_recipe(recipe_dict, 2)
