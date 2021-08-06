import unittest
from src.exercises import Exercise


class TestExercise(unittest.TestCase):

    def setUp(self):
        self.obj = Exercise()

    def test_reverse_list(self):
        expected = [5, 4, 3, 2, 1]
        actual = self.obj.reverse_list([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

        expected = [6, 5, 4, 3, 2, 1]
        actual = self.obj.reverse_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(expected, actual)

    def test_count_digits(self):
        number = 123
        expected = 3
        actual = self.obj.count_digits(number)
        self.assertEqual(expected, actual)

    def tearDown(self):
        del self.obj
