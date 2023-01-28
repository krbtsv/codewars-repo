import unittest

from katas.kyu_8.string_cleaning import string_clean, string_clean_second_solution, string_clean_third_solution, \
    string_clean_fourth_solution


class StringCleanTestCase(unittest.TestCase):
    def test_string_clean(self):
        self.assertEqual(string_clean(""), "")
        self.assertEqual(string_clean("! !"), "! !")
        self.assertEqual(string_clean("123456789"), "")
        self.assertEqual(string_clean("(E3at m2e2!!)"), "(Eat me!!)")
        self.assertEqual(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"), "Dsa cdsc csa!!! I Am cool!")
        self.assertEqual(string_clean("A1 A1! AAA   3J4K5L@!!!"), "A A! AAA   JKL@!!!")
        self.assertEqual(string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"), "Adgre Asad! AAA fvfdvJKL@")
        self.assertEqual(string_clean("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "),
                         "Addsadds A  $$sad! AAAe fKL@ ")
        self.assertEqual(string_clean("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "),
                         "Addsadds A  $$sa!d! A!A!Ae$ f## ")
        self.assertEqual(string_clean("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"),
                         "My \"messy\" data issues! Will they ever, ever be solved?")
        self.assertEqual(string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"),
                         "Why can't we buy the good software? #cheapskates")

    def test_string_clean_second_solution(self):
        self.assertEqual(string_clean_second_solution(""), "")
        self.assertEqual(string_clean_second_solution("! !"), "! !")
        self.assertEqual(string_clean_second_solution("123456789"), "")
        self.assertEqual(string_clean_second_solution("(E3at m2e2!!)"), "(Eat me!!)")
        self.assertEqual(string_clean_second_solution("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"),
                         "Dsa cdsc csa!!! I Am cool!")
        self.assertEqual(string_clean_second_solution("A1 A1! AAA   3J4K5L@!!!"), "A A! AAA   JKL@!!!")
        self.assertEqual(string_clean_second_solution("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"),
                         "Adgre Asad! AAA fvfdvJKL@")
        self.assertEqual(string_clean_second_solution("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "),
                         "Addsadds A  $$sad! AAAe fKL@ ")
        self.assertEqual(string_clean_second_solution("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "),
                         "Addsadds A  $$sa!d! A!A!Ae$ f## ")
        self.assertEqual(
            string_clean_second_solution("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"),
            "My \"messy\" data issues! Will they ever, ever be solved?")
        self.assertEqual(string_clean_second_solution("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"),
                         "Why can't we buy the good software? #cheapskates")

    def test_string_clean_third_solution(self):
        self.assertEqual(string_clean_third_solution(""), "")
        self.assertEqual(string_clean_third_solution("! !"), "! !")
        self.assertEqual(string_clean_third_solution("123456789"), "")
        self.assertEqual(string_clean_third_solution("(E3at m2e2!!)"), "(Eat me!!)")
        self.assertEqual(string_clean_third_solution("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"),
                         "Dsa cdsc csa!!! I Am cool!")
        self.assertEqual(string_clean_third_solution("A1 A1! AAA   3J4K5L@!!!"), "A A! AAA   JKL@!!!")
        self.assertEqual(string_clean_third_solution("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"),
                         "Adgre Asad! AAA fvfdvJKL@")
        self.assertEqual(string_clean_third_solution("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "),
                         "Addsadds A  $$sad! AAAe fKL@ ")
        self.assertEqual(string_clean_third_solution("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "),
                         "Addsadds A  $$sa!d! A!A!Ae$ f## ")
        self.assertEqual(
            string_clean_third_solution("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"),
            "My \"messy\" data issues! Will they ever, ever be solved?")
        self.assertEqual(string_clean_third_solution("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"),
                         "Why can't we buy the good software? #cheapskates")

    def test_string_clean_fourth_solution(self):
        self.assertEqual(string_clean_fourth_solution(""), "")
        self.assertEqual(string_clean_fourth_solution("! !"), "! !")
        self.assertEqual(string_clean_fourth_solution("123456789"), "")
        self.assertEqual(string_clean_fourth_solution("(E3at m2e2!!)"), "(Eat me!!)")
        self.assertEqual(string_clean_fourth_solution("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"),
                         "Dsa cdsc csa!!! I Am cool!")
        self.assertEqual(string_clean_fourth_solution("A1 A1! AAA   3J4K5L@!!!"), "A A! AAA   JKL@!!!")
        self.assertEqual(string_clean_fourth_solution("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"),
                         "Adgre Asad! AAA fvfdvJKL@")
        self.assertEqual(string_clean_fourth_solution("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "),
                         "Addsadds A  $$sad! AAAe fKL@ ")
        self.assertEqual(string_clean_fourth_solution("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "),
                         "Addsadds A  $$sa!d! A!A!Ae$ f## ")
        self.assertEqual(
            string_clean_fourth_solution("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"),
            "My \"messy\" data issues! Will they ever, ever be solved?")
        self.assertEqual(string_clean_fourth_solution("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"),
                         "Why can't we buy the good software? #cheapskates")
