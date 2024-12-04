import tkinter as tk
from TM.TuringMachine import TuringMachine

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Turing Machine GUI")
        self.tm = None

        self.input_label = tk.Label(master, text="Input String:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.search_label = tk.Label(master, text="Element to Search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(master)
        self.search_entry.pack()

        self.run_button = tk.Button(master, text="Run", command=self.run_tm)
        self.run_button.pack()

        self.result_text = tk.Text(master, height=5, width=40)
        self.result_text.pack()
        self.result_text.config(state="disabled")

    def run_tm(self):
        input_string = self.input_entry.get()
        search_element = self.search_entry.get()

        alphabet_symbols = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        states = ['q_start', 'q_search', 'q_accept', 'q_reject']
        initial_state = 'q_start'
        final_states = ['q_accept', 'q_reject']

        self.tm = TuringMachine(input_string, states, initial_state, final_states, alphabet_symbols, search_element)

        self.tm.transitions.add_transition('q_start', '_', 'q_reject', '_', 'R')
        for symbol in alphabet_symbols:
            self.tm.transitions.add_transition('q_start', symbol, 'q_search', symbol, 'R')

        self.tm.transitions.add_transition('q_search', '_', 'q_reject', '_', 'R')
        for symbol in alphabet_symbols:
            if symbol == self.tm.target_symbol:
                self.tm.transitions.add_transition('q_search', symbol, 'q_accept', symbol, 'R')
            else:
                self.tm.transitions.add_transition('q_search', symbol, 'q_search', symbol, 'R')

        self.tm.current_state = initial_state
        try:
            self.tm.run()
            result_message = "Simulation completed.\n"
            if self.tm.current_state == 'q_accept':
                found_position = self.tm.tape.head_position
                result_message += f"Element found at position {found_position}!"
            elif self.tm.current_state == 'q_reject':
                result_message += "Element not found."
            else:
                result_message += "Stopped without reaching a final state."
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_message)
            self.result_text.config(state="disabled")
        except Exception as e:
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(e))
            self.result_text.config(state="disabled")

root = tk.Tk()
gui = TuringMachineGUI(root)
root.mainloop()