import unittest

from katas.kyu_4.string_mix import mix, mix_second_solution


class MixTestCase(unittest.TestCase):
    def test_mix(self):
        self.assertEqual(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        self.assertEqual(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
                         '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        self.assertEqual(mix("looping is fun but dangerous", "less dangerous than coding"),
                         "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        self.assertEqual(mix(" In many languages", " there's a pair of functions"),
                         "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        self.assertEqual(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        self.assertEqual(mix("codewars", "codewars"), "")
        self.assertEqual(mix("A generation must confront the looming ", "codewarrs"),
                         "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")

    def test_mix_second_solution(self):
        self.assertEqual(mix_second_solution("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        self.assertEqual(mix_second_solution("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
                         '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        self.assertEqual(mix_second_solution("looping is fun but dangerous", "less dangerous than coding"),
                         "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        self.assertEqual(mix_second_solution(" In many languages", " there's a pair of functions"),
                         "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        self.assertEqual(mix_second_solution("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        self.assertEqual(mix_second_solution("codewars", "codewars"), "")
        self.assertEqual(mix_second_solution("A generation must confront the looming ", "codewarrs"),
                         "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
