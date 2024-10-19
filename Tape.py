
class Tape:
    def __init__(self, initial_tape=None):
        self.tape = initial_tape if initial_tape else []
        self.position = 0

    def read(self):
        if self.position < len(self.tape):
            return self.tape[self.position]
        else:
            return '_'

    def write(self, symbol):
        if self.position < len(self.tape):
            self.tape[self.position] = symbol
        else:
            self.tape.append(symbol)

    def move_left(self):
        self.position -= 1

    def move_right(self):
        self.position += 1

    def __str__(self):
        return ''.join(self.tape)