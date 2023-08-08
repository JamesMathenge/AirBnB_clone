#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class that defines common attributes/methods for classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
        )

    def save(self):
        """Update public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: dictionary containing key-value pairs of instance attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
