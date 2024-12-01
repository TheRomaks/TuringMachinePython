
class Alphabet:
    def __init__(self, symbols):
        self.symbols = symbols
        self.blank_symbol = '_'

    def is_valid_symbol(self, symbol):
        return symbol in self.symbols or symbol == self.blank_symbol

    def __iter__(self):
        return iter(self.symbols)