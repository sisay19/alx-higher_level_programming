#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest
import io
import sys
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInit(unittest.TestCase):
    """Test Square initialization."""

    def test_square_inherits(self):
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_init_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_init_xy_id(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(5, 1, "2")

    def test_boolean_size(self):
        with self.assertRaises(TypeError):
            Square(True)

    def test_y_value_error_negative(self):
        """Test Square(1, -2) raises ValueError for x."""
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_x_value_error_negative(self):
        """Test Square(1, 2, -3) raises ValueError for y."""
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")


class TestSquareSizeProperty(unittest.TestCase):
    """Test the size property."""

    def test_get_size(self):
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_set_size(self):
        s = Square(5)
        s.size = 20
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_set_size_invalid(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.size = -1


class TestSquareStr(unittest.TestCase):
    """Test __str__ method."""

    def test_str(self):
        s = Square(5, 1, 3, 42)
        self.assertEqual(str(s), "[Square] (42) 1/3 - 5")


class TestSquareUpdate(unittest.TestCase):
    """Test update method."""

    def test_update_args(self):
        s = Square(5, 5, 5, 5)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_partial_args(self):
        s = Square(5, 5, 5, 5)
        s.update(89, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 5)   # unchanged

    def test_update_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(size=10, x=0)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 0)

    def test_update_args_override_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(1, 2, size=99)  # args present, so kwargs ignored
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)

    def test_update_invalid_type(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "2")


class TestSquareToDictionary(unittest.TestCase):
    """Test to_dictionary method."""

    def test_keys(self):
        s = Square(10, 2, 1, 9)
        d = s.to_dictionary()
        self.assertCountEqual(d.keys(), ['id', 'size', 'x', 'y'])

    def test_values(self):
        s = Square(7, 1, 2, 8)
        d = s.to_dictionary()
        self.assertEqual(d['id'], 8)
        self.assertEqual(d['size'], 7)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 2)

    def test_dict_type(self):
        s = Square(1)
        self.assertIsInstance(s.to_dictionary(), dict)


class TestSquareDisplay(unittest.TestCase):
    """Test display method."""

    def capture_display(self, obj):
        capture = io.StringIO()
        sys.stdout = capture
        obj.display()
        sys.stdout = sys.__stdout__
        return capture.getvalue()

    def test_display_no_offset(self):
        s = Square(2)
        self.assertEqual(self.capture_display(s), "##\n##\n")

    def test_display_with_xy(self):
        s = Square(2, 1, 1)
        self.assertEqual(self.capture_display(s), "\n ##\n ##\n")


class TestSquareArea(unittest.TestCase):
    """Test area method (inherited)."""

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_after_update(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.area(), 100)


class TestSquareSaveLoadFile(unittest.TestCase):
    """Test save_to_file and load_from_file on Square class."""

    def setUp(self):
        """Remove JSON files before each test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_None(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")


if __name__ == "__main__":
    unittest.main()
