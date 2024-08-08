# import random
from components import MenuItemRepository, MealGenerator


repository = MenuItemRepository(
    "first_week\\final_project_1\\salad.json",
    "first_week\\final_project_1\\carb.json",
    "first_week\\final_project_1\\soup.json",
    "first_week\\final_project_1\\extra.json",
    "first_week\\final_project_1\\protein.json",
    "first_week\\final_project_1\\meal.json",
)

meal_generator = MealGenerator(repository)
meal = meal_generator.generate_meal(False, True, True)
print("finishhh")


# WEEK_DAYS = [menu_del_dia.get_meal(False, False, False)]

# for i in range(0, 4):
#     WEEK_DAYS.append(menu_del_dia.get_meal(False, False, True))

# random.shuffle(WEEK_DAYS)

# meal1 = menu_del_dia.get_meal(False, True, True)
# print("End")
