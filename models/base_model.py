#!/usr/bin/python3
"""The implementation for the base model for the AirBnB clone."""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """The constructor method of the class."""
        self.id = (str)(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """User-friendly string representation of the class."""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Updates the updated_at public instance attribute-
        -with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values-
        -of __dict__ of the instance.
        """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict
