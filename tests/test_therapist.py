import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.therapist import Therapist


class TestTherapist(unittest.TestCase):

    def test_therapist_creation(self):
        therapist = Therapist()
        self.assertIsNotNone(therapist)


if __name__ == '__main__':
    unittest.main()