class Transition:
    def __init__(self, next_state, symbol_to_write, direction):
        self.next_state = next_state
        self.symbol_to_write = symbol_to_write
        self.direction = direction