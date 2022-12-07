import unittest
from katas.kyu_7.complementary_dna import dna_strand, dna_strand_second_solution


class DNAStrandTestCase(unittest.TestCase):
    def test_dna_strand(self):
        self.assertEqual(dna_strand('AAAA'), 'TTTT')
        self.assertEqual(dna_strand('ATTGC'), 'TAACG')
        self.assertEqual(dna_strand('GTAT'), 'CATA')

    def test_dna_strand_second_solution(self):
        self.assertEqual(dna_strand_second_solution('AAAA'), 'TTTT')
        self.assertEqual(dna_strand_second_solution('ATTGC'), 'TAACG')
        self.assertEqual(dna_strand_second_solution('GTAT'), 'CATA')
