import re


class Card:
    """Represents the card model"""

    def __init__(self, word, pronunciation, definition, example):
        self.word = word
        self.pronunciation = pronunciation
        self.definition = definition
        self.example = example

    def __word_in_example_to_bold(self): 
        # Finds the word of the card in the example and wrap it in a bold tag,
        # returning a new string in that format
        word = re.search(f'{self.word}.*?\w*', self.example, re.IGNORECASE).group()
        return self.example.replace(word, f'<b>{word}</b>')

    def __handle_semicolon(self, string: str):
        # Puts double quotes in the string to escape semicolon
        if ';' in string:
            return f'"{string}"'
        return string

    def to_anki_txt_format(self):
        """Return the card in a string format that the Anki can imports"""
        front = self.__handle_semicolon(f'{self.__word_in_example_to_bold()}')
        back = self.__handle_semicolon(f'<b>{self.word} /{self.pronunciation}/'
                                       f'</b><br> {self.definition}')

        return (f'{front}; {back}')

