import api
import tkinter as tk
from dataclasses import dataclass, field
from gui.base_widget import AbstractBaseWidget

NO_BUTTON = "NO_BUTTON"

@dataclass
class ButtonLayout:
    width: int
    buttons: list[str]
    size_overrides: dict = field(default_factory=dict)

LAYOUT_STANDARD = ButtonLayout(4, 
                ["AC",  "CE", "%", "/",
                 "7",   "8",  "9", "x",
                 "4",   "5",  "6", "-",
                 "1",   "2",  "3", "+",
                 "+/-", "0",  ".", "="])

LAYOUT_NO_NEGATE = ButtonLayout(4,
                ["AC",      "CE", "%", "/",
                 "7",       "8",  "9", "x",
                 "4",       "5",  "6", "-",
                 "1",       "2",  "3", "+",
                 "0",  ".", "="],
                 {(2, 4): (2,1)})

LAYOUT_NO_NUMBERS = ButtonLayout(5,
                ["AC", "CE", "%", ".", "=",
                 "/", "x", "-", "+",],
                 {(4,0): (1,2)})

def calc_button(root, calculator: api.Calculator, display_text): 
    button = tk.Button(root, text=display_text, command=lambda: calculator.input_button(display_text))
    return button

class CalculatorButtons(AbstractBaseWidget):
    def _create_layout(self, window_resolution):
        aspect_ratio = window_resolution[0] / window_resolution[1]
        self.create_buttons(LAYOUT_STANDARD)
    
    def _update(self):
        pass

    def create_buttons(self, layout: ButtonLayout):
        for i, label in enumerate(layout.buttons):
            if label == NO_BUTTON:
                continue
            x = i%layout.width
            y = int(i/layout.width)
            size_x = 1
            size_y = 1
            if (x,y) in layout.size_overrides:
                size_x, size_y = layout.size_overrides[(x,y)]
            
            button = calc_button(self.frame, self.calculator, label)
            button.grid(column=x, row=y, sticky=tk.NSEW, columnspan=size_x, rowspan=size_y)
        
        for i in range(layout.width):
            self.frame.grid_columnconfigure(i, uniform="calc_buttons", weight=1)
        
        for i in range(int(len(layout.buttons)/layout.width)):
            self.frame.grid_rowconfigure(i, weight=1)