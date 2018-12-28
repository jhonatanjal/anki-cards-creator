from anki_cards_creator.card import Card

file_name = 'anki_cards.txt'
def write(*cards: Card):
    """Writes the card in a file"""
    with open(file_name, 'w') as f_obj:
        for card in cards:
            f_obj.write(card.to_anki_txt_format() + '\n')
