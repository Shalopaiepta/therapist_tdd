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
    def test_get_result_returns_string(self):
        therapist = Therapist()
        result = therapist.get_result([False, False])
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    def test_get_result_temperature_no_cough_returns_cold(self):
        therapist = Therapist()
        result = therapist.get_result([True, False])
        self.assertEqual(result, "Простуда")


if __name__ == '__main__':
    unittest.main()