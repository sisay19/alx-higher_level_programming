#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest
import io
import sys
import os                                   # <-- ADD THIS IMPORT
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

    # --- ADD THESE TWO NEW TESTS HERE ---
    def test_y_value_error_negative(self):
        """Test Square(1, -2) raises ValueError for y."""
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_x_value_error_negative(self):
        """Test Square(1, 2, -3) raises ValueError for x."""
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")
    # --- END OF NEW TESTS ---


# ... (keep the other classes: TestSquareSizeProperty, TestSquareStr, etc.)


# --- ADD THIS ENTIRE NEW CLASS AT THE END OF THE FILE ---
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
# --- END OF NEW CLASS ---


if __name__ == "__main__":
    unittest.main()
