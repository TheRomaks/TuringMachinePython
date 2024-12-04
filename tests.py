import unittest

from TM.Alphabet import Alphabet
from TM.Tape import Tape
from TM.Transition import Transition
from TM.TuringMachine import TuringMachine

class TestAlphabet(unittest.TestCase):
    def test_init(self):
        symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        alphabet = Alphabet(symbols)
        self.assertEqual(alphabet.symbols, symbols)
        self.assertEqual(alphabet.blank_symbol, '_')

    def test_is_valid_symbol(self):
        symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        alphabet = Alphabet(symbols)
        self.assertTrue(alphabet.is_valid_symbol('0'))
        self.assertTrue(alphabet.is_valid_symbol('_'))
        self.assertFalse(alphabet.is_valid_symbol('a'))

    def test_iter(self):
        symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        alphabet = Alphabet(symbols)
        self.assertEqual(list(alphabet), list(symbols))

class TestTape(unittest.TestCase):
    def test_init(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)
        self.assertEqual(tape.tape, list(input_string))
        self.assertEqual(tape.head_position, 0)
        self.assertEqual(tape.blank_symbol, '_')

    def test_read(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)
        self.assertEqual(tape.read(), '0')
        tape.head_position = len(input_string)
        self.assertEqual(tape.read(), '_')

    def test_write(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)

        initial_head_position = tape.head_position
        tape.write('X')
        self.assertEqual(tape.tape[initial_head_position], 'X')
        self.assertEqual(len(tape.tape), len(input_string))

        tape.head_position = len(input_string)
        tape.write('X')
        self.assertEqual(tape.tape[-1], 'X')
        self.assertEqual(len(tape.tape), len(input_string) + 1)

    def test_move_left_and_right(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)
        tape.move_right()
        self.assertEqual(tape.head_position, 1)
        tape.move_left()
        self.assertEqual(tape.head_position, 0)

    def test_display(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)
        tape.display()

    def test_str(self):
        input_string = "011342343575876"
        alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        tape = Tape(input_string, alphabet)
        self.assertEqual(str(tape), input_string)

class TestTransition(unittest.TestCase):
    def test_init(self):
        transition = Transition()
        self.assertEqual(transition.transitions, {})

    def test_add_transition(self):
        transition = Transition()
        transition.add_transition('q_start', '0', 'q_search', '0', 'R')
        self.assertIn(('q_start', '0'), transition.transitions)
        self.assertEqual(transition.transitions[('q_start', '0')], ('q_search', '0', 'R'))

    def test_get_transition(self):
        transition = Transition()
        transition.add_transition('q_start', '0', 'q_search', '0', 'R')
        next_state, symbol_to_write, direction = transition.get_transition('q_start', '0')
        self.assertEqual(next_state, 'q_search')
        self.assertEqual(symbol_to_write, '0')
        self.assertEqual(direction, 'R')

    def test_get_transition_key_error(self):
        transition = Transition()
        with self.assertRaises(KeyError):
            transition.get_transition('q_start', '0')

class TestTuringMachine(unittest.TestCase):
    def setUp(self):
        self.alphabet = Alphabet({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        self.states = ['q_start', 'q_search', 'q_accept', 'q_reject']
        self.initial_state = 'q_start'
        self.final_states = ['q_accept', 'q_reject']
        self.input_string = "011342343575876"
        self.target_symbol = '8'
        self.tm = TuringMachine(self.input_string, self.states, self.initial_state, self.final_states, self.alphabet.symbols, self.target_symbol)

        self.tm.transitions.add_transition('q_start', '_', 'q_reject', '_', 'R')
        for symbol in self.alphabet.symbols:
            self.tm.transitions.add_transition('q_start', symbol, 'q_search', symbol, 'R')

        self.tm.transitions.add_transition('q_search', '_', 'q_reject', '_', 'R')
        for symbol in self.alphabet.symbols:
            if symbol == self.target_symbol:
                self.tm.transitions.add_transition('q_search', symbol, 'q_accept', symbol, 'R')
            else:
                self.tm.transitions.add_transition('q_search', symbol, 'q_search', symbol, 'R')

    def test_init(self):
        self.assertEqual(self.tm.states, self.states)
        self.assertEqual(self.tm.initial_state, self.initial_state)
        self.assertEqual(self.tm.final_states, self.final_states)
        self.assertEqual(self.tm.current_state, self.initial_state)
        self.assertEqual(self.tm.alphabet.symbols, self.alphabet.symbols)
        self.assertEqual(self.tm.tape.tape, list(self.input_string))
        self.assertEqual(self.tm.target_symbol, self.target_symbol)

    def test_step(self):
        self.tm.step()
        self.assertEqual(self.tm.current_state, 'q_search')
        self.assertEqual(self.tm.tape.head_position, 1)

    def test_run(self):
        self.tm.run()
        self.assertIn(self.tm.current_state, self.final_states)

    def test_run_invalid_input(self):
        self.input_string = "0113a23433575876"
        self.tm = TuringMachine(self.input_string, self.states, self.initial_state, self.final_states, self.alphabet.symbols, self.target_symbol)
        with self.assertRaises(ValueError):
            self.tm.run()

if __name__ == '__main__':
    unittest.main()
