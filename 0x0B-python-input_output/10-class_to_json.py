#!/usr/bin/python3
"""
    6-from_json_string.py
    Function that writes an Object to \
    a text file, using a JSON representation.
"""
import json


def class_to_json(obj):
    """Function that writes an Object to \
    a text file, using a JSON representation."""
    return json.dumps(obj.__dict__)
