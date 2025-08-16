import tkinter as tk
from gui import button, display
from api import calculator as calc

if __name__ == "__main__":
    c = calc.Calculator()
    main = tk.Tk()
    main.title("Calculator")

    calc_display = display.CalculatorDisplay(c)
    calc_display.create_gui(main)
    calc_display.frame.pack(fill=tk.BOTH,expand=True,side=tk.TOP,padx=10,pady=(10,0))

    calc_buttons = button.CalculatorButtons(c)
    calc_buttons.create_gui(main)
    calc_buttons.frame.pack(fill=tk.BOTH,expand=True,side=tk.BOTTOM,padx=10,pady=(0,10))
    
    while True:
        calc_buttons.update()
        calc_display.update()
        main.update_idletasks()
        main.update()