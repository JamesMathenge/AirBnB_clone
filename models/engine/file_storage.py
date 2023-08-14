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
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                classes = self.classes()
                obj_dict = {k: classes[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
