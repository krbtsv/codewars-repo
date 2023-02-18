import unittest

from katas.kyu_6.remove_the_parentheses import remove_parentheses, remove_parentheses_second_solution, \
    remove_parentheses_third_solution


class RemoveParenthesesTestCase(unittest.TestCase):
    def test_remove_parentheses(self):
        self.assertEqual(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        self.assertEqual(remove_parentheses("example (unwanted thing) example"), "example  example")
        self.assertEqual(remove_parentheses("a (bc d)e"), "a e")
        self.assertEqual(remove_parentheses("a(b(c))"), "a")
        self.assertEqual(remove_parentheses("hello example (words(more words) here) something"),
                         "hello example  something")
        self.assertEqual(remove_parentheses("(first group) (second group) (third group)"), "  ")

    def test_remove_parentheses_second_solution(self):
        self.assertEqual(remove_parentheses_second_solution("example(unwanted thing)example"), "exampleexample")
        self.assertEqual(remove_parentheses_second_solution("example (unwanted thing) example"), "example  example")
        self.assertEqual(remove_parentheses_second_solution("a (bc d)e"), "a e")
        self.assertEqual(remove_parentheses_second_solution("a(b(c))"), "a")
        self.assertEqual(remove_parentheses_second_solution("hello example (words(more words) here) something"),
                         "hello example  something")
        self.assertEqual(remove_parentheses_second_solution("(first group) (second group) (third group)"), "  ")

    def test_remove_parentheses_third_solution(self):
        self.assertEqual(remove_parentheses_third_solution("example(unwanted thing)example"), "exampleexample")
        self.assertEqual(remove_parentheses_third_solution("example (unwanted thing) example"), "example  example")
        self.assertEqual(remove_parentheses_third_solution("a (bc d)e"), "a e")
        self.assertEqual(remove_parentheses_third_solution("a(b(c))"), "a")
        self.assertEqual(remove_parentheses_third_solution("hello example (words(more words) here) something"),
                         "hello example  something")
        self.assertEqual(remove_parentheses_third_solution("(first group) (second group) (third group)"), "  ")
