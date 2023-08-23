spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for food in spicy_foods:
        food_names.append(food["name"])
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append({
                'name': food['name'],
                'cuisine': food["cuisine"],
                'heat_level' : food["heat_level"]
                })
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        emoji = food["heat_level"] * "🌶"
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {emoji}')
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return {
                "name": food["name"],
                "cuisine": food["cuisine"],
                "heat_level": food["heat_level"]
            }

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        emoji = food["heat_level"] * "🌶"
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {emoji}')

def get_average_heat_level(spicy_foods):
    average_heat = (sum(food["heat_level"] for food in spicy_foods)) / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
