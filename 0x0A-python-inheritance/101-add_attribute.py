#!/usr/bin/python3
"""
    101-add_attribute module
    Function that adds a new attribute to an object if it’s possible
"""


def add_attribute(cla, attri, value):
    """Function that adds a new attribute to an object if it's possible"""
    if not(hasattr(obj, '__dict__')):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
