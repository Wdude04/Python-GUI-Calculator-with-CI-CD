from api import calculator as calc
import tkinter as tk

LAYOUT_STANDARD = ["AC",  "CE", "%", "/",
                   "7",   "8",  "9", "x",
                   "4",   "5",  "6", "-",
                   "1",   "2",  "3", "+",
                   "+/-", "0",  ".", "="]

def calc_button(root, calculator: calc.Calculator, display_text): 
    button = tk.Button(root, text=display_text, command=lambda: calculator.input_button(display_text))
    return button

class CalculatorButtons:
    def __init__(self, calculator: calc.Calculator):
        self.calculator = calculator
        self.frame = None

    def create_gui(self, root, layout=LAYOUT_STANDARD, width=4):
        self.frame = tk.Frame(root)

        for i, label in enumerate(layout):
            button = calc_button(self.frame, self.calculator, label)
            button.grid(column=i%width, row=int(i/width), sticky=tk.NSEW)
        
        for i in range(width):
            self.frame.grid_columnconfigure(i, uniform="calc_buttons", weight=1)
        
        for i in range(int(len(layout)/width)):
            self.frame.grid_rowconfigure(i, weight=1)
    
    def update(self):
        pass