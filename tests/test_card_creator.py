import unittest
from unittest.mock import patch
from anki_cards_creator.card import Card
from anki_cards_creator.card_creator import ask_for_card_info, create_card


class CardCreatorTestCase(unittest.TestCase):
    """Tests for 'card_creator.py'."""

    def setUp(self):
        """Create a card for all the tests"""
        self.user_input = [
            'frightfully',
            'ˈfraɪtfəli',
            'as submodifier Very (used for emphasis)',
            'it was frightfully hot',
        ]

        card = Card('frightfully',
                    'ˈfraɪtfəli',
                    'as submodifier Very (used for emphasis)',
                    'it was frightfully hot')
        self.card = card

    def test_ask_for_card_info(self):
        """Test if the function get user input properly"""
        with patch('builtins.input', side_effect=self.user_input):
            card = Card(*ask_for_card_info())
        self.assertEqual(card.__dict__, self.card.__dict__)

    def test_create_card(self):
        """Test that a card object is created properly"""
        with patch('builtins.input', side_effect=self.user_input):
            card = create_card()
        self.assertEqual(card.__dict__, self.card.__dict__)

