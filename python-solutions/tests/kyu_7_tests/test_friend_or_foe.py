import unittest

from katas.kyu_7.friend_or_foe import friend


class FriendTestCase(unittest.TestCase):
    def test_friend(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
        self.assertEqual(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        self.assertEqual(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]),
                         ["Jimm", "Cari", "aret"])
