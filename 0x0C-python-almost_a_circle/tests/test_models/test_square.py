import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_size_getter_setter(self):
        s = Square(5, 2, 3, 99)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_str(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")

    def test_update(self):
        s = Square(5, 2, 3, 4)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(size=2, x=3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        s.update(y=1, size=3, x=2, id=90)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.id, 90)
        s.update(x=1, y=2, size=4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.size, 4)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 4)
        expected_dict = {"id": 4, "x": 2, "size": 5, "y": 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
