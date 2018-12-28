import unittest
from anki_cards_creator.card import Card
import anki_cards_creator.card_writer as card_writer

class CardsWriterTestCase(unittest.TestCase):
    """Tests for 'card_writer.py'."""

    def setUp(self):
        card = Card('owe',
                    'ō',
                    ('Have an obligation to pay or repay (something,'
                    'especially money) in return for something received.'),
                    'I owe you for the taxi')
        self.card = card

    def test_write_card(self):
        """Test if the card is write in the file prorperly"""
        card_writer.write(self.card)
        with open(card_writer.file_name) as f_obj:
            card_txt = f_obj.readline().strip()
        
        self.assertEqual(card_txt, self.card.to_anki_txt_format())

    def test_write_motiples_cards(self):
        """Test the more the one card is writer properly"""
        card = Card('frightfully',
                    'ˈfraɪtfəli',
                    'as submodifier Very (used for emphasis)',
                    'it was frightfully hot')
        card_writer.write(card, self.card)

        with open(card_writer.file_name) as f_obj:
            cards_txt = f_obj.readlines()
        
        self.assertEqual(len(cards_txt), 2)
        self.assertIn(card.to_anki_txt_format() + '\n', cards_txt)        
        self.assertIn(self.card.to_anki_txt_format() + '\n', cards_txt)        
