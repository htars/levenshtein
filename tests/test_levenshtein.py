import unittest
from levenshtein import Levenshtein


class LevenshteinTest(unittest.TestCase):
    
    def test_levenshtein_exact_match(self):
        s = 'aaa'
        t = 'aaa'
        expected = 1.0
        actual = Levenshtein.calc_similarity(s, t)
        self.assertEqual(expected, actual)
