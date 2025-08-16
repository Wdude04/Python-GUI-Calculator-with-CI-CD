from api import calculator as calc
import tkinter as tk

class CalculatorDisplay:
    def __init__(self, calculator: calc.Calculator):
        self.calculator = calculator
        self.frame = None
        self.upper_entry = None
        self.lower_entry = None
    
    def create_gui(self, root):
        self.frame = tk.Frame(root)
        self.upper_entry = tk.Entry(self.frame, state=tk.DISABLED, justify=tk.RIGHT)
        self.lower_entry = tk.Entry(self.frame, state=tk.DISABLED, justify=tk.RIGHT)
        self.upper_entry.grid(row=0, sticky=tk.NSEW)
        self.lower_entry.grid(row=1, sticky=tk.NSEW)
    
    def update(self):
        self.upper_entry.configure(state=tk.NORMAL)
        self.lower_entry.configure(state=tk.NORMAL)

        self.upper_entry.delete(0,tk.END)
        self.lower_entry.delete(0,tk.END)

        if self.calculator.current_part == "first":
            self.lower_entry.insert(0,self.calculator.equation_first)
        elif self.calculator.current_part == "last":
            self.upper_entry.insert(0,self.calculator.equation_first + " " + self.calculator.equation_type)
            self.lower_entry.insert(0,self.calculator.equation_last)

        self.upper_entry.configure(state=tk.DISABLED)
        self.lower_entry.configure(state=tk.DISABLED)

