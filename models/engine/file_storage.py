#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from datetime import datetime
import os
import models


class FileStorage:
    """
    This class manages serialization and deserialization
    of objects to/from JSON files.
    It provides methods to save
    and load objects from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing
        objects serialized in JSON format.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects,
        or all objects of a specific class.

        Args:
            cls (class, optional): The class
            to filter objects. Defaults to None.

        Returns:
            dict: A dictionary containing objects.
        """
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects in __objects to JSON format and saves.
        """
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserializes objects from the JSON file stores them in __objects.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    if cls_name in FileStorage.CLASSES:
                        self.__objects[key] = FileStorage.CLASSES[cls_name](
                            **value)
        except FileNotFoundError:
            pass


FileStorage.CLASSES = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
    }
