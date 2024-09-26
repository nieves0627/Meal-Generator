from fastapi import FastAPI

from components import MenuItemRepository, MealGenerator

app = FastAPI()

folder_path = "C:\\Users\\Juli\\Desktop\\Juliana\\Programacion\\repositories\\Meal-Generator\\folder_path"
repository = MenuItemRepository(folder_path)

meal_generator = MealGenerator(repository)
meal = meal_generator.generate_meal(with_extra=False,
                                    with_soup=True,
                                    with_meat=False)
result = meal.to_string()
print(result)


# @app.get("/{component}")
# async def get_components_meal(component):

#     file = open(f"folder_path\\{component}.json")
#     return json.load(file)


@app.get("/{with_extra}/{with_soup}/{with_meat}")
async def get_menu(with_extra: bool, with_soup: bool, with_meat: bool):

    folder_path = "C:\\Users\\Juli\\Desktop\\Juliana\\Programacion\\repositories\\Meal-Generator\\folder_path"
    repository = MenuItemRepository(folder_path)

    meal_generator = MealGenerator(repository)
    meal = meal_generator.generate_meal(with_extra, with_soup, with_meat)
    return meal.to_string()
