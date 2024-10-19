from Tape import Tape
from Transition import Transition

class TuringMachine:
    def __init__(self, states, initial_state, final_states):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.current_state = initial_state
        self.tape = Tape()

    def step(self):
        current_symbol = self.tape.read()
        transition = Transition.get_transition(self.current_state, current_symbol)
        if transition:
            next_state, symbol_to_write, direction = transition.get_transition_details()
            self.tape.write(symbol_to_write)
            self.current_state = next_state
            if direction == 'L':
                self.tape.move_left()
            elif direction == 'R':
                self.tape.move_right()
        else:
            raise Exception("No transition defined for current state and symbol")

    def run(self, input_string):
        self.tape = Tape(list(input_string))
        while self.current_state not in self.final_states:
            self.step()
        return self.tape.tape



