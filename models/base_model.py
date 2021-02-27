#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
""" THE BASE MODEL FOR THE AIRBNB """


class BaseModel:
    """ The basic of our first website"""

    def __init__(self, *args, **kwargs):
        """ initialize my variables """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) == 0:
            models.storage.new(self)
        else:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, form)
                else:
                    self.__dict__[i] = j

    def save(self):
        """ get the update time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ get the dict infos """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__clss.__name__
        return my_dict

    def __str__(self):
        """ the format printing """
        Name = self.__class.__name__
        return "[{}] ({}) {}".format(Name, self.id, self.__dict__)
