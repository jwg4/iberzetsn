# coding=utf-8

import unittest

from iberzetsn import yiddish_to_roman, roman_to_yiddish


class TestRoundTripFromYiddish(unittest.TestCase):
    def do_round_trip_and_compare(self, word):
        roman = yiddish_to_roman(word)
        result = roman_to_yiddish(roman)
        self.assertEqual(result, word)

    def test_two_words(self):
        self.do_round_trip_and_compare("דער שטאׇף")


class TestRoundTripFromRoman(unittest.TestCase):
    def do_round_trip_and_compare(self, word):
        yiddish = roman_to_yiddish(word)
        result = yiddish_to_roman(yiddish)
        self.assertEqual(result, word)

    def test_word(self):
        self.do_round_trip_and_compare("nakht")

    def test_another_word(self):
        self.do_round_trip_and_compare("rusland")

    def test_yet_another_word(self):
        self.do_round_trip_and_compare("hafn")
