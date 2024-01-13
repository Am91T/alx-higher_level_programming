import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    def setUp(self):
        # Clear existing files before each test
        for filename in ["Rectangle.json", "Square.json", "Rectangle.csv", "Square.csv"]:
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        # Clear created files after each test
        for filename in ["Rectangle.json", "Square.json", "Rectangle.csv", "Square.csv"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"key": "value"}]), '[{"key": "value"}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string(self):
        json_str = '[{"key": "value"}]'
        self.assertEqual(Base.from_json_string(json_str), [{"key": "value"}])

    def test_create(self):
        r_dict = {'id': 1, 'width': 10, 'height': 5}
        r = Rectangle.create(**r_dict)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

        s_dict = {'id': 2, 'size': 8}
        s = Square.create(**s_dict)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_load_from_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

    def test_draw(self):
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(5)
        list_rectangles = [r1]
        list_squares = [s1]

        Base.draw(list_rectangles, list_squares)

if __name__ == "__main__":
    unittest.main()
