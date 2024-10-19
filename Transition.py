class Transition:

    def __init__(self):
        # self.current_state = current_state
        # self.current_symbol = current_symbol
        # self.next_state = next_state
        # self.symbol_to_write = symbol_to_write
        # self.direction = direction
        # self.transitions[(current_state, current_symbol)] = self
        self.transitions = {}

    def add_transition(self, current_state, symbol, next_state, write_symbol, direction):
        self.transitions[(current_state, symbol)] = (next_state, write_symbol, direction)

    def get_transition(self, current_state, symbol):
        if (current_state, symbol) not in self.transitions:
            raise KeyError(f"No transition defined for state '{current_state}' with symbol '{symbol}'")
        return self.transitions[(current_state, symbol)]