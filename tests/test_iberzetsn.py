import unittest

from iberzetsn import yiddish_to_roman, roman_to_yiddish


class TestYiddishToRoman(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(yiddish_to_roman("שול"), "shul")

    def test_simple_word_2(self):
        self.assertEqual(yiddish_to_roman("װוּרשט"), "vursht")


class TestRomanToYiddish(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(roman_to_yiddish("yiddish"), "ייִדיש")

    def test_simple_two_word_phrase(self):
        self.assertEqual(roman_to_yiddish("dos broyt"), "דאׇס ברױט")


class TestRoundTripFromYiddish(unittest.TestCase):
    def do_round_trip_and_compare(self, word):
        roman = yiddish_to_roman(word)
        result = roman_to_yiddish(roman)
        self.assertEqual(result, word)

    def test_word(self):
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
