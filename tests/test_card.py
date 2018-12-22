import unittest
import anki_cards_creator
from anki_cards_creator.card import Card


class TestCard(unittest.TestCase):
    """Test for the class Card"""

    def setUp(self):
        """Create a card for all the tests"""
        card = Card('frightfully',
                    'ˈfraɪtfəli', 
                    'as submodifier Very (used for emphasis)', 
                    'it was frightfully hot')
        self.card = card

    def test_to_anki_txt_format(self):
        """Test that the string in the format that Anki reads is returned"""

        anki_str_expected = ('it was <b>frightfully</b> hot; '
                             '<b>frightfully /ˈfraɪtfəli/</b><br> '
                             'as submodifier Very (used for emphasis)')
        anki_str_returned = self.card.to_anki_txt_format()
        self.assertEqual(anki_str_returned, anki_str_expected)

