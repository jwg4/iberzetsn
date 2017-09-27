import unittest

from iberzetsn import yiddish_to_roman, roman_to_yiddish


class TestYiddishToRoman(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(yiddish_to_roman("שול"), "shul")

class TestRomanToYiddish(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(roman_to_yiddish("yiddish"), "ייִדיש")
