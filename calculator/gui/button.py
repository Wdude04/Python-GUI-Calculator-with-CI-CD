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

LAYOUT_STANDARD_TALL = ButtonLayout(4, 
                ["AC",  "CE", "%", "/",
                 "7",   "8",  "9", "x",
                 "4",   "5",  "6", "-",
                 "1",   "2",  "3", "+",
                 "+/-", "0",  ".", "="])

LAYOUT_STANDARD_WIDE = ButtonLayout(5,
                ["AC",  "7",   "8",  "9", "/",
                 "CE",  "4",   "5",  "6", "x",
                 "%",   "1",   "2",  "3", "-",
                 "+/-", "0",   ".",  "=", "+"])

def calc_button(root, calculator: api.Calculator, display_text): 
    button = tk.Button(root, text=display_text, command=lambda: calculator.input_button(display_text))
    return button

class CalculatorButtons(AbstractBaseWidget):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.prev_column_count = 0

    def _create_layout(self, window_resolution):
        aspect_ratio = window_resolution[0] / window_resolution[1]
        if aspect_ratio > 1:
            self.create_buttons(LAYOUT_STANDARD_WIDE)
            self.prev_column_count = LAYOUT_STANDARD_WIDE.width
        else:
            self.create_buttons(LAYOUT_STANDARD_TALL)
            self.prev_column_count = LAYOUT_STANDARD_TALL.width
    
    def _destroy_layout(self):
        super()._destroy_layout()
        for i in range(self.prev_column_count):
            self.frame.columnconfigure(i, weight=0)
    
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
            self.frame.grid_columnconfigure(i, weight=1)
        
        for i in range(int(len(layout.buttons)/layout.width)):
            self.frame.grid_rowconfigure(i, weight=1)