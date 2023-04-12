import unittest
from utils import dicts


class TestDict(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: "Name1", 2: "Name2", 3: "Name3"}, 1, "git"), "Name1")
        self.assertEqual(dicts.get_val({}, 1, "test"), "test")
        self.assertEqual(dicts.get_val({1: "Name1", 2: "Name2", 3: "Name3"}, 5, "git"), "git")
        self.assertEqual(dicts.get_val({1: "Name1", 2: "Name2", 3: "Name3"}, 3), "Name3")
        self.assertEqual(dicts.get_val({}, 1), "git")
        self.assertEqual(dicts.get_val({1: "Name1", 2: "Name2", 3: None}, 3), "Значение None")

