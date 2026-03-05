import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.symptom_database import SymptomDatabase


class TestSymptomDatabase(unittest.TestCase):

    def test_symptom_database_creation(self):
        db = SymptomDatabase()
        self.assertIsNotNone(db)
    def test_get_question_0_returns_string(self):
        db = SymptomDatabase()
        result = db.get_question(0)
        self.assertIsInstance(result,str)
        self.assertGreater(len(result),0)


if __name__ == '__main__':
    unittest.main()