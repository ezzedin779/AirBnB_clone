#!/usr/bin/python3
import json
from models.base_model import BaseModel
""" FILE STORAGE ... """


class FileStorage:
    """ Storage engine of my little airbnb"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        name = obj.__class.__name__
		FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        my_dict = FileStorage.__objects
        omy_dict = {i: my_dict[i].to_dict() for i in my_dict.keys()}
        with open(FileStorage.__file_path, "w") as fil:
            json.dump(omy_dict, fil)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) """
        try:
            with open(FileStorage.file_path) as fil:
                omy_dict = json.load(fil)
                for i in omy_dict.values():
                    name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(name)(**i))
        expect FileNotFoundError:
            return
