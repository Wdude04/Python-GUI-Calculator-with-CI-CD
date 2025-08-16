import api
import tkinter as tk
from abc import ABC, abstractmethod

class AbstractBaseWidget(ABC):
    def __init__(self, calculator: api.Calculator):
        self.parent = None
        self.frame = None
        self.calculator = calculator
        self.prev_window_resolution = (0,0)
    
    def get_window_resolution(self):
        return (self.parent.winfo_width(), self.parent.winfo_height())

    def init_gui(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.prev_window_resolution = self.get_window_resolution()
        self._create_layout(self.prev_window_resolution)
    
    @abstractmethod
    def _create_layout(self, window_resolution: tuple):
        pass

    def _destroy_layout(self):
        for child in self.frame.winfo_children():
            child.destroy()

    @abstractmethod
    def _update(self):
        pass

    def update(self):
        window_resolution = self.get_window_resolution()
        if self.prev_window_resolution != window_resolution:
            self._destroy_layout()
            self._create_layout(window_resolution)
        self._update()
        self.prev_window_resolution = window_resolution