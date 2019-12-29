import unittest
import anki_cards_creator
from anki_cards_creator.card import Card


class TestCard(unittest.TestCase):
    """Test for the class Card"""

    def test_to_anki_txt_format(self):
        """Test that the string in the format that Anki reads is returned"""
        card = Card(
            "frightfully",
            "ˈfraɪtfəli",
            "as submodifier Very (used for emphasis)",
            "it was frightfully hot",
        )

        anki_str_expected = (
            "it was <b>frightfully</b> hot; "
            "<b>frightfully /ˈfraɪtfəli/</b><br> "
            "as submodifier Very (used for emphasis)"
        )
        anki_str_returned = card.to_anki_txt_format()
        self.assertEqual(anki_str_returned, anki_str_expected)

    def test_escape_semicolon(self):
        """Test that double quotes are put in the string to escape semicolon"""
        card = Card(
            "mocking",
            "ˈmɑkɪŋ",
            "Making fun of someone or something in a cruel way; derisive.",
            "The ruthless scientist changed from mocking to sad.",
        )

        expected = (
            "The ruthless scientist changed from <b>mocking</b> to sad.; "
            '"<b>mocking /ˈmɑkɪŋ/</b><br> Making fun of someone or '
            'something in a cruel way; derisive."'
        )

        self.assertEqual(card.to_anki_txt_format(), expected)

    def test_ignore_case(self):
        """Test that to_anki_txt_format method is case insensitive"""
        card = Card(
            "henceforth",
            "ˌhensˈfôrTH",
            "From this time on or from that time on.",
            "Henceforth in the winter everyone will just have to suffer.",
        )

        expected = (
            "<b>Henceforth</b> in the winter everyone will just have "
            "to suffer.; <b>henceforth /ˌhensˈfôrTH/</b><br> "
            "From this time on or from that time on."
        )

        self.assertEqual(card.to_anki_txt_format(), expected)
