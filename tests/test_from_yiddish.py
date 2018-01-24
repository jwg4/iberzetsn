import unittest

from iberzetsn import yiddish_to_roman


class TestYiddishToRoman(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(yiddish_to_roman("שול"), "shul")

    def test_simple_word_2(self):
        self.assertEqual(yiddish_to_roman("װוּרשט"), "vursht")

    def test_simple_word_3(self):
        self.assertEqual(yiddish_to_roman("שטײט"), "shteyt")

    def test_exceptional_word(self):
        self.assertEqual(yiddish_to_roman("אויף"), "af")

    def test_exceptional_word_2(self):
        self.assertEqual(yiddish_to_roman("ייִדיש"), "yiddish")

    def test_word_with_compound_vowels(self):
        self.assertEqual(yiddish_to_roman("דזשוכע"), "dzhukhe")

    @unittest.skip("Longer phrase with several difficult words.")
    def test_phrase_with_punctuation(self):
        self.assertEqual(
            yiddish_to_roman("שטײט אױף, איר אַלע, װער ווי שקלאַפֿן"),
            "Shteyt af, ayr ole shklaven"
        )
