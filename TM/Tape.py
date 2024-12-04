
class Tape:
    def __init__(self, input_string,alphabet):
        self.tape = list(input_string)
        self.head_position = 0
        self.blank_symbol = alphabet.blank_symbol

    def read(self):
        if self.head_position < 0 or self.head_position >= len(self.tape):
            return self.blank_symbol
        return self.tape[self.head_position]

    def write(self, symbol):
        if self.head_position < 0 or self.head_position >= len(self.tape):
            if self.head_position < 0:
                self.tape.insert(0, symbol)
                self.head_position = 0
            else:
                self.tape.append(symbol)
        else:
            self.tape[self.head_position] = symbol

    def move_left(self):
        self.head_position -= 1

    def move_right(self):
        self.head_position += 1

    def display(self):
        print(''.join(self.tape))
        print(' ' * self.head_position + '^')

    def __str__(self):
        return ''.join(self.tape)