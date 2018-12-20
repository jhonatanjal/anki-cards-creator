import re


class Card:
    """Represents the card model"""

    def __init__(self, word, pronunciation, definition, example):
        self.word = word
        self.pronunciation = pronunciation
        self.definition = definition
        self.example = example

    #TODO to think of a better name for the method. __word_in_example_to_bold(self)?
    def __wrap_in_bold_tag(self): 
        """
        Finds the word of the card in the example and wrap it in a bold's tag
        """
        word = re.search(f'{self.word}.*?\w*', self.example).group()
        return self.example.replace(word, f'<b>{word}</b>')

    def to_anki_txt_format(self):
        """Return the card in a string format that the Anki can imports"""
        return (f'{self.__wrap_in_bold_tag()}; "<b>{self.word}'
                f' /{self.pronunciation}/</b><br> {self.definition}"')

