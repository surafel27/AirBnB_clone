#!/usr/bin/python3
""" the file storage module """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    public_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        file_dict = {}
        for key, value in FileStorage.__objects.items():
            file_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as myFile:
            json.dump(file_dict, myFile, indent=2)

    def classes_dict(self):
        """collection of classes"""
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        return classes_dict

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        reload_dict = {}
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as r:
                reload_dict = json.load(r)
            for key, value in reload_dict.items():
                # obj = FileStorage.public_dict[value["__class__"]](**value)
                obj = eval(value["__class__"])(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
