import unittest

from iberzetsn import roman_to_yiddish


class TestRomanToYiddish(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(roman_to_yiddish("yiddish"), "ייִדיש")

    def test_simple_two_word_phrase(self):
        self.assertEqual(roman_to_yiddish("dos broyt"), "דאׇס ברױט")

    def test_word_with_implied_vowels(self):
        self.assertEqual(roman_to_yiddish("khaverte"), "חבֿרטע")

    def test_word_with_straightforward_vowels(self):
        self.assertEqual(roman_to_yiddish("golmeser"), "גאׇלמעסער")

    def test_word_with_melupm_vov(self):
        self.assertEqual(roman_to_yiddish("tuung"), "טוּונג")

    def test_word_with_hyphen(self):
        self.assertEqual(roman_to_yiddish("zoo-gortn"), "זאׇאׇ־גאׇרטן")
