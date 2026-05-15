#!/usr/bin/python3
"""Unit tests for Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBaseInit(unittest.TestCase):
    """Test instantiation."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_private_class_attr(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_id_increment_after_set(self):
        b = Base()
        b2 = Base(100)
        b3 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Test to_json_string static method."""

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_valid_dict_list(self):
        r = Rectangle(10, 7, 2, 8, 1)
        d = r.to_dictionary()
        json_str = Base.to_json_string([d])
        self.assertEqual(json_str, json.dumps([d]))

    def test_multiple_dicts(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_str = Base.to_json_string([d1, d2])
        self.assertEqual(json_str, json.dumps([d1, d2]))


class TestBaseSaveToFile(unittest.TestCase):
    """Test save_to_file class method."""

    def setUp(self):
        for f in ["Base.json", "Rectangle.json", "Square.json"]:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_save_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_rectangle_objects(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        expected = json.dumps([r.to_dictionary()])
        self.assertEqual(content, expected)

    def test_save_square_objects(self):
        s = Square(5, 1, 2, 99)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = f.read()
        expected = json.dumps([s.to_dictionary()])
        self.assertEqual(content, expected)


class TestBaseFromJsonString(unittest.TestCase):
    """Test from_json_string static method."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        list_input = [{'id': 1, 'width': 2, 'height': 3}]
        json_str = json.dumps(list_input)
        result = Base.from_json_string(json_str)
        self.assertEqual(result, list_input)

    def test_returns_list(self):
        self.assertIsInstance(Base.from_json_string("[]"), list)


class TestBaseCreate(unittest.TestCase):
    """Test create class method."""

    def test_create_rectangle(self):
        d = {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2}
        r = Rectangle.create(**d)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)

    def test_create_square(self):
        d = {'id': 100, 'size': 7, 'x': 1, 'y': 0}
        s = Square.create(**d)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 100)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 0)

    def test_create_no_args(self):
        r = Rectangle.create()
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test load_from_file class method."""

    def setUp(self):
        for f in ["Rectangle.json", "Square.json"]:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_file_not_exist(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_after_save(self):
        r1 = Rectangle(10, 5, 0, 0, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in loaded))
        self.assertEqual(loaded[0].id, 1)
        self.assertEqual(loaded[1].id, 2)

    def test_square_load(self):
        s = Square(6, 2, 3, 42)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertIsInstance(loaded[0], Square)
        self.assertEqual(loaded[0].size, 6)


if __name__ == "__main__":
    unittest.main()
