class Transition:
    def __init__(self):
        self.transitions = {}

    def add_transition(self, current_state, symbol, next_state, write_symbol, direction):
        if direction not in ['L', 'R','N']:
            raise ValueError(f"Direction '{direction}' must be either 'L' or 'R' or 'N'")
        self.transitions[(current_state, symbol)] = (next_state, write_symbol, direction)

    def get_transition(self, current_state, symbol):
        if (current_state, symbol) not in self.transitions:
            raise KeyError(f"No transition defined for state '{current_state}' with symbol '{symbol}'")
        return self.transitions[(current_state, symbol)]
