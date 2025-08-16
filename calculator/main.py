import tkinter as tk
import api
import gui

class App:
    def __init__(self):
        self.calculator = api.Calculator()
        self.window = tk.Tk()
        self.display = None
        self.buttons = None
    
    def key_handler(self, event):
        if event.char.isdigit():
            self.calculator.add_digit(event.char)
        elif event.char in set(item.value for item in api.Operator):
            self.calculator.set_operator(event.char)
        elif event.char == "=" or event.keysym == "Return":
            if self.calculator.current_part == "last":
                self.calculator.solve()
        elif event.char == ".":
            self.calculator.add_decimal()
        elif event.keysym == "BackSpace":
            self.calculator.clear_entry()
            

    def create_gui(self):
        self.window.title("Calculator")

        self.display = gui.CalculatorDisplay(self.calculator)
        self.buttons = gui.CalculatorButtons(self.calculator)

        self.display.init_gui(self.window)
        self.buttons.init_gui(self.window)
        
        self.display.frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,padx=10,pady=(10,0))
        self.buttons.frame.pack(fill=tk.BOTH,expand=True,side=tk.BOTTOM,padx=10,pady=(0,10))
        
        self.window.bind("<Key>", self.key_handler)
    
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
