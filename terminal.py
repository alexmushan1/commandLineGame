import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class TerminalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal Emulator")

        # Create a ScrolledText widget for output
        self.output_widget = ScrolledText(root, wrap=tk.WORD, height=20, width=80)
        self.output_widget.pack(padx=10, pady=10)

        # Create an Entry widget for input
        self.input_widget = tk.Entry(root, width=80)
        self.input_widget.pack(padx=10, pady=10)
        self.input_widget.bind("<Return>", self.process_input)

        # Redirect print function to custom print
        self.original_print = print
        self.print = self.custom_print

        # Set input() functionality
        self.input_value = tk.StringVar()
        self.waiting_for_input = False

    def custom_print(self, *args, **kwargs):
        text = " ".join(map(str, args))
        self.output_widget.insert(tk.END, text + "\n")
        self.output_widget.yview(tk.END)

    def process_input(self, event):
        self.input_value.set(self.input_widget.get())
        self.input_widget.delete(0, tk.END)
        self.custom_print(f"> {self.input_value.get()}")
        if self.waiting_for_input:
            self.waiting_for_input = False

    def custom_input(self, prompt=""):
        self.custom_print(prompt, end="")
        self.waiting_for_input = True
        self.input_widget.focus()
        self.root.wait_variable(self.input_value)
        return self.input_value.get()

    def close_window(self):
        # Add code here to handle window closing event
        return False
    def run(self):
        pass

