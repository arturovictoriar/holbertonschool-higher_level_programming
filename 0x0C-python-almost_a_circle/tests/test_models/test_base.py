#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
from models.base import Base


class TestBaseclass(unittest.TestCase):
    def setUp(self):
        self.inst = Base(5)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_nb_objs_yes(self):
        self.assertEqual(self.inst._Base__nb_objects, 0)

    def test_nb_objs_no(self):
        self.inst = Base()
        self.assertEqual(self.inst._Base__nb_objects, 1)

    def test_id(self):
        self.assertEqual(self.inst.id, 5)
