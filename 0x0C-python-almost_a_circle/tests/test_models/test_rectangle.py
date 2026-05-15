#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
import io
import sys
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
        # Booleans are ints, but type(True) is bool, not int, so should fail
        with self.assertRaises(TypeError):
            Rectangle(True, 5)


class TestRectangleArea(unittest.TestCase):
    """Test area method."""

    def test_area_small(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        r = Rectangle(1000, 1000)
        self.assertEqual(r.area(), 1000000)

    def test_area_after_update(self):
        r = Rectangle(2, 10)
        r.width = 5
        self.assertEqual(r.area(), 50)


class TestRectangleDisplay(unittest.TestCase):
    """Test display method using stdout capture."""

    def capture_display(self, rect):
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        sys.stdout = sys.__stdout__
        return capture.getvalue()

    def test_display_no_offset(self):
        r = Rectangle(2, 2)
        output = self.capture_display(r)
        self.assertEqual(output, "##\n##\n")

    def test_display_with_x_offset(self):
        r = Rectangle(2, 2, 2, 0)
        output = self.capture_display(r)
        self.assertEqual(output, "  ##\n  ##\n")

    def test_display_with_y_offset(self):
        r = Rectangle(2, 2, 0, 2)
        output = self.capture_display(r)
        self.assertEqual(output, "\n\n##\n##\n")

    def test_display_with_xy_offset(self):
        r = Rectangle(2, 3, 2, 1)
        output = self.capture_display(r)
        expected = "\n" + "  ##\n" * 3
        self.assertEqual(output, expected)


class TestRectangleStr(unittest.TestCase):
    """Test __str__ representation."""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdate(unittest.TestCase):
    """Test update method."""

    def test_update_args_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_partial_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)   # unchanged

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, x=7)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 7)

    def test_update_kwargs_invalid_key_ignored(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(area=99)   # ignored
        self.assertEqual(r.width, 10)

    def test_update_args_skip_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, height=999)   # args present, kwargs ignored
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_update_type_error_via_args(self):
        r = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            r.update(1, "2")


class TestRectangleToDictionary(unittest.TestCase):
    """Test to_dictionary method."""

    def test_dict_keys(self):
        r = Rectangle(10, 2, 1, 1, 1)
        d = r.to_dictionary()
        self.assertCountEqual(d.keys(), ['id', 'width', 'height', 'x', 'y'])

    def test_dict_values(self):
        r = Rectangle(10, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 3)
        self.assertEqual(d['y'], 4)
        self.assertEqual(d['id'], 5)

    def test_dict_return_type(self):
        r = Rectangle(1, 1)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
