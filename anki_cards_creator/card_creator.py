from anki_cards_creator.card import Card

def ask_for_card_info():
    """Ask user for the card infos"""
    print('Enter with the cards info')

    word = input('\tWord: ')
    pronunciation = input('\tPronunciation: ')
    definition = input('\tDefinition: ')
    exemple = input('\tExemple: ')
    return word, pronunciation, definition, exemple

def create_card():
    """Returns a card object"""
    card = Card(*ask_for_card_info())
    return card
