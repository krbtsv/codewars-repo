import unittest

from katas.kyu_5.extract_the_domain_name_from_a_url import domain_name, domain_name_second_solution


class DomainName(unittest.TestCase):
    def test_domain_name(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")

    def test_domain_name_second_solution(self):
        self.assertEqual(domain_name_second_solution("http://google.com"), "google")
        self.assertEqual(domain_name_second_solution("http://google.co.jp"), "google")
        self.assertEqual(domain_name_second_solution("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name_second_solution("https://youtube.com"), "youtube")
