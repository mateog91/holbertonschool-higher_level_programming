#!/usr/bin/python3
"""module with class Base"""


from models.rectangle import Rectangle


class Base:
    """class Base"""
    # creat class attribute number of objects
    __nb_object = 0

    def __init__(self, id=None):
        """Initializes id to the given input id or to an automated counter

        Args:
            id (int): [unique id of object]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    def integer_validator(self, name, value):
        """validates value as integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:

        Args: list_objs
            list_objs (list):  is a list of instances who inherits of Base
                - example: list of Rectangle or list of Square instances
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as myFile:
            if list_objs is None:
                return myFile.write("[]")
            lst_dictionary = [obj.to_dictionary() for obj in list_objs]
            txt = cls.to_json_string(lst_dictionary)
            return myFile.write(txt)

    @staticmethod
    def from_json_string(json_string):
        import json
        """returns the list of the JSON string representation json_string
            If json_string is None or empty, return an empty list

        Args:
            json_string (str): a string representing a list of dictionaries
        """
        lst = json.loads(json_string)
        if lst is None or lst == []:
            return []
        return lst

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set:

            Args:
            dictionary (dict):  must be used as **kwargs of the method update
            """
        if cls.__name__ == Rectangle:
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances:

            Description:
                Creates instances from JSON file and returns a list with the
                created objects"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                list_dict = cls.from_json_string(myFile.read())
                list_obj = [cls.create(**c_dict) for c_dict in list_dict]
                return list_obj
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Creates a CSV file with attributes of an object

        Args:
            list_objs ([Rectangle/Square]): List with instances of Base Class
                Rectangles or Squares"
        """
        import csv
        filename = cls.__name__ + ".csv"
        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']

        # pass from list of objects to list of dictionaries
        lst_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for dict in lst_dict:
                writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        """Creates objects from a CSV file with attributes of the objects


        Returns:
            [Rectangle or Square]: List of instances of rectangles squares
        """
        import csv
        filename = cls.__name__ + ".csv"
        with open(filename, mode="r", newline='') as file:
            reader = csv.DictReader(file)

            lst_dict = [row for row in reader]

        for dict in lst_dict:
            for element in dict:
                dict[element] = int(dict[element])

        return [cls.create(**dict) for dict in lst_dict]
