import unittest

from katas.kyu_6.encrypt_this import encrypt_this, encrypt_this_second_solution


class EncryptThisTestCase(unittest.TestCase):
    def test_encrypt_this(self):
        self.assertEqual(encrypt_this(""), "")
        self.assertEqual(encrypt_this("A"), "65")
        self.assertEqual(encrypt_this("A wise old owl lived in an oak"),
                         "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
        self.assertEqual(encrypt_this("The more he saw the less he spoke"),
                         "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
        self.assertEqual(encrypt_this("The less he spoke the more he heard"),
                         "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
        self.assertEqual(encrypt_this("Why can we not all be like that wise old bird"),
                         "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri")
        self.assertEqual(encrypt_this("Thank you Piotr for all your help"),
                         "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")

    def test_encrypt_this_second_solution(self):
        self.assertEqual(encrypt_this_second_solution(""), "")
        self.assertEqual(encrypt_this_second_solution("A"), "65")
        self.assertEqual(encrypt_this_second_solution("A wise old owl lived in an oak"),
                         "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
        self.assertEqual(encrypt_this_second_solution("The more he saw the less he spoke"),
                         "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
        self.assertEqual(encrypt_this_second_solution("The less he spoke the more he heard"),
                         "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
        self.assertEqual(encrypt_this_second_solution("Why can we not all be like that wise old bird"),
                         "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri")
        self.assertEqual(encrypt_this_second_solution("Thank you Piotr for all your help"),
                         "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")
