import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.diagnosis_engine import DiagnosisEngine


class TestDiagnosisEngine(unittest.TestCase):

    def test_diagnosis_engine_creation(self):
        engine = DiagnosisEngine()
        self.assertIsNotNone(engine)


if __name__ == '__main__':
    unittest.main()