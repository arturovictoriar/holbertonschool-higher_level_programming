#!/usr/bin/python3
"""
    base.py module
"""
import json


class Base:
    """ Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialitation method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)
