import unittest

from katas.kyu_8.simple_validation_of_a_username_with_regex import validate_usr, validate_usr_second_solution


class ValidateUsrTestCase(unittest.TestCase):
    def test_validate_usr(self):
        self.assertEqual(validate_usr('asddsa'), True)
        self.assertEqual(validate_usr('a'), False)
        self.assertEqual(validate_usr('Hass'), False)
        self.assertEqual(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
        self.assertEqual(validate_usr(''), False)
        self.assertEqual(validate_usr('____'), True)
        self.assertEqual(validate_usr('012'), False)
        self.assertEqual(validate_usr('p1pp1'), True)
        self.assertEqual(validate_usr('asd43 34'), False)
        self.assertEqual(validate_usr('asd43_34'), True)

    def test_validate_usr_second_solution(self):
        self.assertEqual(validate_usr_second_solution('asddsa'), True)
        self.assertEqual(validate_usr_second_solution('a'), False)
        self.assertEqual(validate_usr_second_solution('Hass'), False)
        self.assertEqual(validate_usr_second_solution('Hasd_12assssssasasasasasaasasasasas'), False)
        self.assertEqual(validate_usr_second_solution(''), False)
        self.assertEqual(validate_usr_second_solution('____'), True)
        self.assertEqual(validate_usr_second_solution('012'), False)
        self.assertEqual(validate_usr_second_solution('p1pp1'), True)
        self.assertEqual(validate_usr_second_solution('asd43 34'), False)
        self.assertEqual(validate_usr_second_solution('asd43_34'), True)
