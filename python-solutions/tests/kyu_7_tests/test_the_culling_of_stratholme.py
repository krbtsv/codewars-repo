import unittest

from katas.kyu_7.the_culling_of_stratholme import (purify,
                                                   purify_second_solution)


class PurifyTestCase(unittest.TestCase):
    def test_purify(self):
        self.assertEqual(purify("CHILI"), "C")
        self.assertEqual(purify("The eradication of the citizens of Stratholme"),
                         "The eraan of the ens of Stratholme")

        self.assertEqual(purify("Kimi Imimi goes to our school"), "goes to our school")
        self.assertEqual(purify("In heaven all the interesting people are missing"),
                         "heaven all the teresg people are g")

        self.assertEqual(purify("5I5 i39i9i1 139iii39i i5i9i 1"), "13 1")
        self.assertEqual(purify("TIL that TIL means Today I learned"), "that means Today learned")
        self.assertEqual(purify("zippity duppity bopity bip ZIPPITY DUPPITY BOPITY BIP"), "y dupy boy Y DUPY BOY")
        self.assertEqual(purify("Six sick hicks nick six slick bricks with picks and sticks"),
                         "k ks k sk bks h ks and sks")
        self.assertEqual(purify("Do not go skiing in the summer"), "Do not go sg the summer")
        self.assertEqual(purify("Id id ieididi eeiiowe diid owodiid"), "ewe owo")

    def test_purify_second_solution(self):
        self.assertEqual(purify_second_solution("CHILI"), "C")
        self.assertEqual(purify_second_solution("The eradication of the citizens of Stratholme"),
                         "The eraan of the ens of Stratholme")

        self.assertEqual(purify_second_solution("Kimi Imimi goes to our school"), "goes to our school")
        self.assertEqual(purify_second_solution("In heaven all the interesting people are missing"),
                         "heaven all the teresg people are g")

        self.assertEqual(purify_second_solution("5I5 i39i9i1 139iii39i i5i9i 1"), "13 1")
        self.assertEqual(purify_second_solution("TIL that TIL means Today I learned"), "that means Today learned")
        self.assertEqual(purify_second_solution("zippity duppity bopity bip ZIPPITY DUPPITY BOPITY BIP"),
                         "y dupy boy Y DUPY BOY")
        self.assertEqual(purify_second_solution("Six sick hicks nick six slick bricks with picks and sticks"),
                         "k ks k sk bks h ks and sks")
        self.assertEqual(purify_second_solution("Do not go skiing in the summer"), "Do not go sg the summer")
        self.assertEqual(purify_second_solution("Id id ieididi eeiiowe diid owodiid"), "ewe owo")
