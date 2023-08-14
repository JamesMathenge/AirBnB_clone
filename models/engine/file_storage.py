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
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
            with open(self.__file_path, "w") as file:
                json.dump(obj_dict, file)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                # TODO: should this overwrite or insert?
                FileStorage.__objects = obj_dict

                def attributes(self):
                    """Returns attributes and their types for classname"""
                    attributes = {
                        "BaseModel":
                        {"id": str,
                         "created_at": datetime.datetime,
                         "updated_at": datetime.datetime},
                        "User":
                        {"email": str,
                         "password": str,
                            "first_name": str,
                         "last_name": str},
                        "State":
                        {"name": str},
                        "City":
                        {"state_id": str,
                         "name": str},
                        "Amenity":
                        {"name": str},
                        "Place":
                        {"city_id": str,
                         "user_id": str,
                            "name": str,
                         "description": str,
                         "number_rooms": int,
                         "number_bathrooms": int,
                         "max_guest": int,
                            "price_by_night": int,
                            "latitude": float,
                         "longitude": float,
                         "amenity_ids": list},
                        "Review":
                        {"place_id": str,
                         "user_id": str,
                         "text": str}
                    }
                    return attributes
