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
        self.assertEqual(result,"У вас есть температура?")
    def test_get_question_1_returns_string(self):
        db= SymptomDatabase()
        result = db.get_question(1)
        self.assertEqual(result,"У вас есть кашель?")
    def test_get_size_returns_2(self):
        db=SymptomDatabase()
        result=db.get_size()
        self.assertEqual(result,2)
        

if __name__ == '__main__':
    unittest.main()