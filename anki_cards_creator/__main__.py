from anki_cards_creator.card_creator import create_card
import anki_cards_creator.card_writer as card_writer
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = []
while True:
    cls()
    print('Welcome to Anki Cards Creator')
    print('Press Ctrl + c to exit\n')

    if len(cards) > 0:
        print(f'{len(cards)} {"cards" if len(cards) > 1 else "card"} created\n')

    try:
        cards.append(create_card())
    except KeyboardInterrupt:
        break

if len(cards) > 0:
    card_writer.write(*cards)
    print(f'\nCards saved in file: {card_writer.file_name}')
else:
    print('\nNo card created')
