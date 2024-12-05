# Создаем экземпляр машины Тьюринга
from TM.Alphabet import Alphabet
from TM.TuringMachine import TuringMachine

alphabet_symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
alphabet = Alphabet(alphabet_symbols)

states = ['q_start', 'q_search', 'q_accept', 'q_reject']
initial_state = 'q_start'
final_states = ['q_accept', 'q_reject']
input_string = "011348343575876"
target_symbol = '8'

tm = TuringMachine(input_string, states, initial_state, final_states, alphabet, target_symbol)


tm.transitions.add_transition('q_start', '_', 'q_reject', '_', 'N')
for symbol in alphabet:
    tm.transitions.add_transition('q_start', symbol, 'q_search', symbol, 'R')

tm.transitions.add_transition('q_search', '_', 'q_reject', '_', 'N')
for symbol in alphabet:
    if symbol == tm.target_symbol:
        tm.transitions.add_transition('q_search', symbol, 'q_accept', symbol, 'N')
    else:
        tm.transitions.add_transition('q_search', symbol, 'q_search', symbol, 'R')

tm.current_state = initial_state

result = tm.run()

print("Позиция:", result)
