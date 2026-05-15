#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
import io
import sys
import os                                   # <-- ADD THIS IMPORT (it's now needed)
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInit(unittest.TestCase):
    """Test Rectangle initialization."""

    def test_valid_init(self):
        r = Rectangle(10, 20, 2, 3, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 99)

    def test_no_id(self):
        r = Rectangle(5, 5)
        self.assertIsNotNone(r.id)

    def test_private_width(self):
        r = Rectangle(5, 5)
        with self.assertRaises(AttributeError):
            print(r.__width)

    def test_width_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("str", 5)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_value_error_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 5)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_value_error_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 5.5)

    # --- ADD THESE TWO NEW TESTS HERE ---
    def test_height_value_error_negative(self):
        """Test Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_value_error_zero(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")
    # --- END OF NEW TESTS ---

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 5, "1")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1, 0)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 5, 0, "2")

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 0, -2)

    def test_boolean_input(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 5)


# ... (keep all other existing classes: TestRectangleArea, TestRectangleDisplay, etc.)


# --- ADD THIS ENTIRE NEW CLASS AT THE END OF THE FILE ---
class TestRectangleSaveLoadFile(unittest.TestCase):
    """Test save_to_file and load_from_file on Rectangle class."""

    def setUp(self):
        """Remove JSON files before each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_None(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
# --- END OF NEW CLASS ---


if __name__ == "__main__":
    unittest.main()
