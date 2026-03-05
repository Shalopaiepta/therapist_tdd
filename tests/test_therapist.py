import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.therapist import Therapist


class TestTherapist(unittest.TestCase):

    def test_therapist_creation(self):
        therapist = Therapist()
        self.assertIsNotNone(therapist)
    def test_ask_all_returns_list_of_correct_length(self):
        therapist = Therapist()
        result = therapist.ask_all([True, False])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()