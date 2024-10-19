from Tape import Tape
from Transition import Transition


class TuringMachine:
    def __init__(self, states, initial_state, final_states, transition_function):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.current_state = initial_state
        self.tape = Tape()

    def step(self):
        current_symbol = self.tape.read()
        transition = self.transition_function.get((self.current_state, current_symbol))
        if transition:
            next_state, symbol_to_write, direction = transition.next_state, transition.symbol_to_write, transition.direction
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

    def __str__(self):
        return f"State: {self.current_state}, Tape: {self.tape}"


# Таблица переходов для инкремента двоичного числа
transition_function = {
    ('q0', '0'): Transition('q0', '0', 'R'),
    ('q0', '1'): Transition('q0', '1', 'R'),
    ('q0', '_'): Transition('q1', '1', 'L'),  # Переход к обработке переноса
    ('q1', '0'): Transition('q1', '1', 'L'),
    ('q1', '1'): Transition('q1', '0', 'L'),
    ('q1', '_'): Transition('qf', '_', 'R'),  # qf - конечное состояние
}

# Создание машины Тьюринга
tm = TuringMachine(states=['q0', 'q1', 'qf'], initial_state='q0', final_states=['qf'], transition_function=transition_function)

# Запуск машины Тьюринга
input_string = "10101"
result = tm.run(input_string)
print("Result:", ''.join(result))