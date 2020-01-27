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

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except:
            return []

        l = []
        with open(str(cls.__name__) + ".json", "r") as f:
            l = cls.from_json_string(f.read())

        num_ins = len(l)
        inst = []
        for y in range(num_ins):
            inst.append(cls.create(**l[y]))

        return inst

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        l = []
        try:
            f = open(str(type(list_objs[0]).__name__) + ".json")
            f.close()
        except:
            with open(str(type(list_objs[0]).__name__) + ".json", "w") as f:
                f.write(cls.to_json_string([]))

        if len(list_objs) == 0:
            with open(str(type(list_objs[0]).__name__) + ".json", "r") as f:
                l = json.loads(f.read())

            with open(str(type(list_objs[0]).__name__) + ".json", "w") as f:
                f.write(cls.to_json_string(l))

        else:
            with open(str(type(list_objs[0]).__name__) + ".json", "r+") as f:
                z = f.read()
                if len(z) == 0:
                    f.write(cls.to_json_string([]))

            with open(str(type(list_objs[0]).__name__) + ".json", "r") as f:
                l = json.loads(f.read())

            with open(str(type(list_objs[0]).__name__) + ".json", "w") as f:
                for el in list_objs:
                    l.append(el.to_dictionary())

                f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)
