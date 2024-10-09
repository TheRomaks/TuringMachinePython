class TuringMachine:
    def __init__(self, tape, target):
        self.tape = list(tape)  # Лента, представлена как список символов
        self.head = 0           # Позиция головки на ленте
        self.state = 'q0'       # Начальное состояние
        self.target = target     # Искомый элемент

    def step(self):
        if self.state == 'q0':
            if self.head < len(self.tape):
                if self.tape[self.head] == self.target:
                    self.state = 'q1'  # Элемент найден
                elif self.tape[self.head] == '#':
                    self.state = 'q2'  # Элемент не найден
                self.head += 1  # Перемещение головки

        elif self.state == 'q1':
            pass

    def run(self):
        while self.state not in ['q1', 'q2']:
            self.step()

    def result(self):
        if self.state == 'q1':
            return "Элемент найден!"
        else:
            return "Элемент не найден."


# Пример использования
tape = "1#0#1#0#"
target ="0"  # Искомый элемент
tm = TuringMachine(tape, target)
tm.run()
print(tm.result())
