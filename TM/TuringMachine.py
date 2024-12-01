from TM.Tape import Tape
from TM.Transition import Transition
from TM.Alphabet import Alphabet
class TuringMachine:
    def __init__(self, tape, states, initial_state, final_states, alphabet, target_symbol):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.current_state = initial_state
        self.alphabet = Alphabet(alphabet)
        self.tape = Tape(tape, self.alphabet)
        self.transitions = Transition()
        self.target_symbol = target_symbol

    def step(self):
        current_symbol = self.tape.read()
        print(f"Current State: {self.current_state}, Read Symbol: '{current_symbol}'")
        self.tape.display()
        try:
            next_state, symbol_to_write, direction = self.transitions.get_transition(self.current_state, current_symbol)
        except KeyError:
            raise Exception("No transition defined for current state and symbol")
        self.tape.write(symbol_to_write)
        print(f"Wrote Symbol: '{symbol_to_write}', Next State: {next_state}, Moving: {direction}")
        self.current_state = next_state
        if direction == 'L':
            self.tape.move_left()
        elif direction == 'R':
            self.tape.move_right()

    def run(self):
        if any(symbol not in self.alphabet.symbols for symbol in self.tape.tape):
            raise ValueError("Input string contains symbols not in the alphabet")
        while self.current_state not in self.final_states:
            try:
                current_symbol = self.tape.read()
                self.step()
                if current_symbol == self.target_symbol:
                    self.current_state = 'q_accept'
                    break
            except Exception as e:
                print(str(e))
                break
        if self.current_state == 'q_accept':
            print("Result: Element found!")
        elif self.current_state == 'q_reject':
            print("Result: Element not found.")
        else:
            print("Result: Stopped without reaching a final state.")
        return self.tape.tape


