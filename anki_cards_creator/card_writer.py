from anki_cards_creator.card import Card
from datetime import datetime

date = datetime.today()
datetime_format = "%d-%m-%Y_%H:%M:%S"
file_name = f"{date.strftime(datetime_format)}_anki_cards.txt"


def write(*cards: Card, file_name=file_name):
    """Writes the card in a file"""
    with open(file_name, "a") as f_obj:
        for card in cards:
            f_obj.write(card.to_anki_txt_format() + "\n")
