import tkinter as tk
from gui import button, display
from api import calculator as calc

if __name__ == "__main__":
    c = calc.Calculator()
    main = tk.Tk()
    main.title = "Calculator"
    main.grid_rowconfigure(0, weight=1)
    main.grid_rowconfigure(1, weight=2)
    main.grid_columnconfigure(0, weight=1)

    calc_display = display.CalculatorDisplay(c)
    calc_display.create_gui(main)
    calc_display.frame.grid(row=0,sticky=tk.NSEW)

    calc_buttons = button.CalculatorButtons(c)
    calc_buttons.create_gui(main)
    calc_buttons.frame.grid(row=1,sticky=tk.NSEW)
    
    while True:
        calc_buttons.update()
        calc_display.update()
        main.update_idletasks()
        main.update()