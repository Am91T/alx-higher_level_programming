import unittest
import io
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(5, 3, 1, 4)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 4)
        self.assertIsNotNone(r.id)

    def test_width_getter_setter(self):
        r = Rectangle(5, 3, 1, 4)
        r.width = 8
        self.assertEqual(r.width, 8)

    def test_height_getter_setter(self):
        r = Rectangle(5, 3, 1, 4)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_x_getter_setter(self):
        r = Rectangle(10, 7)
        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError):
            r.x = "not an integer"
        with self.assertRaises(ValueError):
            r.x = -2

    def test_y_getter_setter(self):
        r = Rectangle(10, 7)
        r.y = 3
        self.assertEqual(r.y, 3)
        with self.assertRaises(TypeError):
            r.y = "not an integer"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(10, 7)
        self.assertEqual(r.area(), 70)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with io.StringIO() as captured_output:
            with contextlib.redirect_stdout(captured_output):
                r.display()
                self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/8 10/7")

    def test_update(self):
        r = Rectangle(10, 7, 2, 8, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)

    def test_to_dictionary(self):
        r = Rectangle(10, 7, 2, 8, 1)
        expected_dict = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
