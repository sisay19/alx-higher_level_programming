#!/usr/bin/python3
"""Module containing the Base class."""
import json
import csv


class Base:
    """The base class for all models in this project.

    Attributes:
        __nb_objects (int): Private class attribute to assign unique IDs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base.

        Args:
            id (int): ID for the instance. If None, auto-assigns an ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries from JSON string representation.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set.

        Args:
            dictionary (dict): Dictionary of attributes to set on the instance.

        Returns:
            Base: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return list of instances from file.

        Returns:
            list: List of instances of the class.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_str = f.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file.

        Args:
            list_objs (list): List of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file to instances.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        inst = cls(1, 1)
                        inst.update(id=int(row[0]), width=int(row[1]),
                                    height=int(row[2]), x=int(row[3]), y=int(row[4]))
                    elif cls.__name__ == "Square":
                        inst = cls(1)
                        inst.update(id=int(row[0]), size=int(row[1]),
                                    x=int(row[2]), y=int(row[3]))
                    instances.append(inst)
                return instances
        except FileNotFoundError:
            return []
