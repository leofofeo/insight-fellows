import unittest
from src.main import return_four

class TestMainFile(unittest.TestCase):

    def test_received_four(self):
        expected = 4
        actual = return_four()
        self.assertEqual(expected, actual)
        self.assertEqual(3, 4)