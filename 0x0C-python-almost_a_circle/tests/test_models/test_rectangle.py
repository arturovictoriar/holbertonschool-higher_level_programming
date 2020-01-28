#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleclass(unittest.TestCase):
    def setUp(self):
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_area(self):
        self.assertEqual(self.inst.area(), 2)

    def out_c(self)
        t = sys.stdout
        sys.stdout = StringIO()
        self.inst.display()
        o = sys.stdout.getvalue()
        

    def test_display(self):
        self.
        self.assertEqual(self.inst.display(), stout)

    def test_id(self):
        self.assertEqual(self.inst.id, 5)

    def test_id_1(self):
        self.inst.id = 0
        inst1 = Rectangle(1, 2)
        inst2 = Rectangle(2, 1)
        inst3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(inst3.id, 3)

    def test_width(self):
        self.assertEqual(self.inst.width, 1)

    def test_height(self):
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        self.assertEqual(self.inst.y, 4)

    def test_raise_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.width = "Fault"

    def test_raise_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.inst.height = "Fault"

    def test_raise_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.inst.x = "Fault"

    def test_raise_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.inst.y = "Fault"

    def test_raise_width_1(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.inst.width = 0

    def test_raise_height_1(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.inst.height = 0

    def test_raise_x_1(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.inst.x = -1

    def test_raise_y_1(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
             self.inst.y = -1
