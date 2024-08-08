"""Meal Component and Generation System

This module provides a comprehensive system for managing and generating meals
composed of various components such as proteins, carbohydrates, salads, soups,
and extra items. It includes classes for representing meal items, a data
repository for storing and retrieving meal component data, and a meal generator
for creating customized meals based on specified criteria.

Key components:
- MealItems: Base class for all meal components
- Repository: Abstract base class for data storage and retrieval
- MenuItemRepository: Concrete implementation of Repository for loading and
  managing meal component data
- ProteinFilter: Utility class for filtering protein items
- Meal: Representation of a complete meal
- MealGenerator: Class for generating customized meals

This module is designed to be flexible and extensible, allowing for easy
addition of new meal components and customization of meal generation logic.
"""


import json
from abc import ABC
import random


class MealItems(ABC):
    """
    Abstract base class for meal items.

    Attributes:
        name (str): The name of the meal item.
    """
    def __init__(self, name: str):
        """
        Initialize a MealItems instance.

        Args:
            name (str): The name of the meal item.
        """
        self.name = name


class Salad(MealItems):
    """
    Represents a salad component of a meal.
    """
    def __init__(self, name: str):
        """
        Initialize a Salad instance.

        Args:
            name (str): The name of the salad.
        """
        super().__init__(name)


class Carb(MealItems):
    """
    Represents a carbohydrate component of a meal.
    """
    def __init__(self, name: str):
        """
        Initialize a Carb instance.

        Args:
            name (str): The name of the carbohydrate.
        """
        super().__init__(name)


class Soup(MealItems):
    """
    Represents a soup component of a meal.
    """
    def __init__(self, name: str):
        """
        Initialize a Soup instance.

        Args:
            name (str): The name of the soup.
        """
        super().__init__(name)


class Extra(MealItems):
    """
    Represents an extra component of a meal.
    """
    def __init__(self, name: str):
        super().__init__(name)


class Protein(MealItems):
    """
    Represents a protein component of a meal.

    Attributes:
        name (str): The name of the protein.
        meat (bool): True if the protein is meat-based, False otherwise.
    """

    def __init__(self, name: str, meat_base: bool):
        """
        Initialize a Protein instance.

        Args:
            name (str): The name of the protein.
            meat_base (bool): True if the protein is meat-based,
            False otherwise.
        """
        super().__init__(name)
        self.meat = meat_base


class Repository(ABC):
    """
    Abstract base class for data repositories.

    Attributes:
        salad_data (list): List to store salad data.
        carb_data (list): List to store carbohydrate data.
        soup_data (list): List to store soup data.
        extra_data (list): List to store extra item data.
        protein_data (list): List to store protein data.
        meal_data (list): List to store meal data.
    """
    salad_data = []
    carb_data = []
    soup_data = []
    extra_data = []
    protein_data = []
    meal_data = []

    def load_salad(self):
        """Load salad data."""
        pass

    def load_carb(self):
        """Load carbohydrate data."""
        pass

    def load_soup(self):
        """Load soup data."""
        pass

    def load_extra(self):
        """Load extra item data."""
        pass

    def load_protein(self):
        """Load protein data."""
        pass

    def load_meal(self):
        """Load meal data."""
        pass

    def get_salad_data(self):
        """Retrieve salad data."""
        pass

    def get_carb_data(self):
        """Retrieve carbohydrate data."""
        pass

    def get_soup_data(self):
        """Retrieve soup data."""
        pass

    def get_extra_data(self):
        """Retrieve extra item data."""
        pass

    def get_protein_data(self) -> list[Protein]:
        """Retrieve protein data."""
        pass

    def get_meal_data(self):
        """Retrieve meal data."""
        pass


class MenuItemRepository(Repository):
    """
    Repository for managing menu items.
    """
    def __init__(
        self, salad_path,
        carb_path, soup_path,
        extra_path, protein_path, meal_path
    ):
        """
        Initialize a MenuItemRepository instance.

        Args:
            salad_path (str): Path to the salad data file.
            carb_path (str): Path to the carbohydrate data file.
            soup_path (str): Path to the soup data file.
            extra_path (str): Path to the extra item data file.
            protein_path (str): Path to the protein data file.
            meal_path (str): Path to the meal data file.
        """
        self.load_salad(salad_path)
        self.load_carb(carb_path)
        self.load_soup(soup_path)
        self.load_extra(extra_path)
        self.load_protein(protein_path)
        self.load_meal(meal_path)

    def load_salad(self, file_path):
        """
        Load salad data from a JSON file.

        Args:
            file_path (str): Path to the salad data JSON file.
        """
        with open(file_path, "r") as file:
            salad_json = json.load(file)
            salads_list = []
            for salad_arg in salad_json:
                salad_instance = Salad(salad_arg)
                salads_list.append(salad_instance)
            self.salad_data = salads_list

    def load_carb(self, file_path):
        """
        Load carbohydrate data from a JSON file.

        Args:
            file_path (str): Path to the carbohydrate data JSON file.
        """
        with open(file_path, "r") as file:
            carb_json = json.load(file)
            carbs_list = []
            for carb_arg in carb_json:
                carb_instance = Carb(carb_arg)
                carbs_list.append(carb_instance)
            self.carb_data = carbs_list

    def load_soup(self, file_path):
        """
        Load soup data from a JSON file.

        Args:
            file_path (str): Path to the soup data JSON file.
        """
        with open(file_path, "r") as file:
            soup_json = json.load(file)
            soups_list = []
            for soup_arg in soup_json:
                soup_instance = Soup(soup_arg)
                soups_list.append(soup_instance)
            self.soup_data = soups_list

    def load_extra(self, file_path):
        """
        Load extra item data from a JSON file.

        Args:
            file_path (str): Path to the extra item data JSON file.
        """
        with open(file_path, "r") as file:
            extra_json = json.load(file)
            extras_list = []
            for extra_arg in extra_json:
                extra_instance = Extra(extra_arg)
                extras_list.append(extra_instance)
            self.extra_data = extras_list

    def load_protein(self, file_path):
        """
        Load protein data from a JSON file.

        Args:
            file_path (str): Path to the protein data JSON file.
        """
        with open(file_path, "r") as file:
            p_json = json.load(file)
            protein_list = []
            for p_args in p_json:
                p_instance = Protein(**p_args)
                protein_list.append(p_instance)
            self.protein_data = protein_list

    def load_meal(self, file_path):
        """
        Load meal data from a JSON file.

        Args:
            file_path (str): Path to the meal data JSON file.
        """
        with open(file_path, "r") as file:
            meal_json = json.load(file)
            meal_list = []
            for meal_args in meal_json:
                meal_instance = Meal(**meal_args)
                meal_list.append(meal_instance)
            self.meal_data = meal_list

    def get_salad_data(self):
        """
        Retrieve the list of salad data.

        Returns:
            list: A list of Salad objects.
        """
        return self.salad_data

    def get_carb_data(self):
        """
        Retrieve the list of carbohydrate data.

        Returns:
            list: A list of Carb objects.
        """
        return self.carb_data

    def get_soup_data(self):
        """
        Retrieve the list of soup data.

        Returns:
            list: A list of Soup objects.
        """
        return self.soup_data

    def get_extra_data(self):
        """
        Retrieve the list of extra item data.

        Returns:
            list: A list of Extra objects.
        """
        return self.extra_data

    def get_protein_data(self):
        """
        Retrieve the list of protein data.

        Returns:
            list: A list of Protein objects.
        """
        return self.protein_data

    def get_meal_data(self):
        """
        Retrieve the list of meal data.

        Returns:
            list: A list of Meal objects.
        """
        return self.meal_data


class ProteinFilter:
    """
    A utility class for filtering protein items.
    """
    @staticmethod
    def filter_protein(with_meat: bool,
                       protein_list: list[Protein]) -> list[Protein]:
        """
        Filter a list of proteins based on whether they are meat-based or not.

        Args:
            with_meat (bool): If True, return meat-based proteins;
            if False, return non-meat proteins. protein_list (list[Protein]):
            The list of proteins to filter.

        Returns:
            list[Protein]: A filtered list of proteins.
        """
        list_protin = []
        for protein in protein_list:
            if protein.meat == with_meat:
                list_protin.append(protein)
        return list_protin


class Meal:
    """
    Represents a complete meal composed of various components.

    Attributes:
        name (str): The name of the meal.
        protein (Protein): The protein component of the meal.
        carb (str): The carbohydrate component of the meal.
        salad (str): The salad component of the meal.
        extra (str, optional): An additional component of the meal.
        soup (str, optional): A soup component of the meal.
    """

    def __init__(
        self,
        name: str,
        protein: Protein,
        carb: Carb,
        salad: Salad,
        extra: Extra = None,
        soup: Soup = None,
    ):
        """
        Initialize a Meal instance.

        Args:
            name (str): The name of the meal.
            protein (Protein): The protein component of the meal.
            carb (str): The carbohydrate component of the meal.
            salad (str): The salad component of the meal.
            extra (str, optional): An additional component of the meal.
            soup (str, optional): A soup component of the meal.
        """

        self.name = name
        self.protein = protein
        self.carb = carb
        self.salad = salad
        self.extra = extra
        self.soup = soup


class MealGenerator:
    """
    A class for generating meals based on specified criteria.
    """
    def __init__(self, repository: Repository):
        """
        Initialize a MealGenerator instance.

        Args:
            repository (Repository): The repository
            containing meal component data.
        """
        self.repository = repository

    def generate_meal(self, with_extra: bool,
                      with_soup: bool,
                      with_meat: bool):
        """
        Generate a meal based on specified criteria.

        Args:
            with_extra (bool): Whether to include an extra item in the meal.
            with_soup (bool): Whether to include soup in the meal.
            with_meat (bool): Whether to include meat-based protein.

        Returns:
            Meal: A generated meal instance.
        """
        meal_arguments = {
            "salad": random.choice(self.repository.get_salad_data()),
            "carb": random.choice(self.repository.get_carb_data()),
        }

        if with_extra:
            meal_arguments["extra"] = random.choice(
                self.repository.get_extra_data())
        if with_soup:
            meal_arguments["soup"] = random.choice(
                self.repository.get_soup_data())

        protein_list = self.repository.get_protein_data()
        protein_list_filtered = ProteinFilter.filter_protein(
            with_meat, protein_list)
        meal_arguments["protein"] = random.choice(protein_list_filtered)

        meal = Meal("meal1", **meal_arguments)

        return meal
