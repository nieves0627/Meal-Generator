# import random
from components import MenuItemRepository, MealGenerator

folder_path = "C:\\Users\\Juli\\Desktop\\Juliana\\Programacion\\study_plan_practice\\first_week\\final_project_1\\folder_path"
repository = MenuItemRepository(folder_path)

meal_generator = MealGenerator(repository)
meal = meal_generator.generate_meal(with_extra=True, with_soup=True, with_meat=True)
message = meal.to_string()
print(message)
print("finishhh")


# WEEK_DAYS = [menu_del_dia.get_meal(False, False, False)]

# for i in range(0, 4):
#     WEEK_DAYS.append(menu_del_dia.get_meal(False, False, True))

# random.shuffle(WEEK_DAYS)

# meal1 = menu_del_dia.get_meal(False, True, True)
# print("End")
