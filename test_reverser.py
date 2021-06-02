import unittest
import reverser


class TestCase(unittest.TestCase):

    def test_reverser_1(self):
        self.assertEqual(reverser.reverse("Hello World"), "World Hello")

    def test_reverser_2(self):
        self.assertEqual(reverser.reverse("My name is Adam."), "Adam is name My.")

    def test_reverser_3(self):
        self.assertEqual(reverser.reverse("Adam is This Hi...."), "Hi... This is Adam.")


if __name__ == '__main__':
    unittest.main(verbosity = 2)
