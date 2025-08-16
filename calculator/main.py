import tkinter as tk
from gui import button, display
from api import calculator as calc

class App:
    def __init__(self):
        self.calculator = calc.Calculator()
        self.window = tk.Tk()
        self.display = None
        self.buttons = None
    
    def create_gui(self):
        self.window.title("Calculator")

        self.display = display.CalculatorDisplay(self.calculator)
        self.buttons = button.CalculatorButtons(self.calculator)

        self.display.create_gui(self.window)
        self.buttons.create_gui(self.window)
        
        self.display.frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,padx=10,pady=(10,0))
        self.buttons.frame.pack(fill=tk.BOTH,expand=True,side=tk.BOTTOM,padx=10,pady=(0,10))
    
    def update(self):
        self.buttons.update()
        self.display.update()
        self.window.update_idletasks()
        self.window.update()
    
    def run(self):
        while True:
            self.update()


if __name__ == "__main__":
    my_app = App()
    my_app.create_gui()
    my_app.run()
