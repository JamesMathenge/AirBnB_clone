#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import datetime
import os
import models


class FileStorage:
    """FileStorage class serializes/deserializes instances to/from JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Set an object in the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    cls = getattr(models, cls_name)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
