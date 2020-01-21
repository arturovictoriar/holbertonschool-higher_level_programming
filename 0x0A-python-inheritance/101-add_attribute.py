#!/usr/bin/python3
"""
    101-add_attribute module
    Function that adds a new attribute to an object if it’s possible
"""


def add_attribute(cla, attri, value):
    """Function that adds a new attribute to an object if it's possible"""
    if hasattr(cla, '__dict__') or hasattr(cla, '__slots__'):
        setattr(cla, attri, value)
    else:
        raise TypeError("can't add new attribute")
