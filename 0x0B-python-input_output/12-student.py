#!/usr/bin/python3
"""
    6-from_json_string.py
    Function that writes an Object to \
    a text file, using a JSON representation.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that writes an Object to \
        a text file, using a JSON representation."""
        attrib = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    attrib[i] = self.__dict__[i]
            if len(attrib) == 0:
                return obj.__dict__
            return attrib
        return self.__dict__
