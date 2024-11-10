import unittest
from utils.mutant import is_mutant
from input_examples import MUTANT_DNA, NON_MUTANT_DNA

class Test_is_mutant_util(unittest.TestCase):
    def test_is_mutant_for_mutant_dna(self):
        result = is_mutant(MUTANT_DNA)
        self.assertTrue(result)
    
    def test_is_non_mutant_for_non_mutant_dna(self):
        result = is_mutant(NON_MUTANT_DNA)
        self.assertFalse(result)

if __name__ == 'main':
    unittest.main()