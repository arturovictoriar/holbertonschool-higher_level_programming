#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry.
   Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
   Public instance method:\
   def integer_validator(self, name, value):\
   that validates value
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self): \
           that raises an Exception with\
           the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:\
           def integer_validator(self, name, value):\
           that validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
