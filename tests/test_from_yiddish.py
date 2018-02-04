# coding=utf-8

import unittest

from iberzetsn import yiddish_to_roman


class TestYiddishToRoman(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(yiddish_to_roman("שול"), "shul")

    def test_simple_word_2(self):
        self.assertEqual(yiddish_to_roman("װוּרשט"), "vursht")

    def test_simple_word_3(self):
        self.assertEqual(yiddish_to_roman("שטײט"), "shteyt")

    def test_simple_word_4(self):
        self.assertEqual(yiddish_to_roman("פֿרום"), "frum")

    def test_exceptional_word(self):
        self.assertEqual(yiddish_to_roman("אויף"), "af")

    def test_exceptional_word_2(self):
        self.assertEqual(yiddish_to_roman("ייִדיש"), "yiddish")

    def test_word_with_compound_vowels(self):
        self.assertEqual(yiddish_to_roman("דזשוכע"), "dzhukhe")

    def test_word_with_compound_vowels_2(self):
        self.assertEqual(yiddish_to_roman("טשיקאַװע"), "tshikave")

    def test_simple_word_with_multiple_compound_sounds(self):
        self.assertEqual(yiddish_to_roman("צװײ"), "tsvey")

    def test_word_with_final_letter(self):
        self.assertEqual(yiddish_to_roman("אַרץ"), "arts")

    @unittest.skip("Hebrew word used in yiddish")
    def test_word_with_hebrew_letters(self):
        self.assertEqual(yiddish_to_roman("תּנ״ך"), "tanakh")

    @unittest.skip("Longer phrase with several difficult words.")
    def test_phrase_with_punctuation(self):
        self.assertEqual(
            yiddish_to_roman("שטײט אױף, איר אַלע, װער ווי שקלאַפֿן"),
            "Shteyt af, ayr ole shklaven"
        )
