import unittest

from machinetranslation import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello").lower(), "bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour").lower(), "hello")

unittest.main()