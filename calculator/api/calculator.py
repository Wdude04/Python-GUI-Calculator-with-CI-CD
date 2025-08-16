from enum import Enum

class Operator(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "x"
    DIVIDE = "/"

ALL_CLEAR = "AC"
CLEAR_ENTRY = "CE"
FLIP_SIGN = "+/-"
DECIMAL = "."
EQ_SIGN = "="

class Calculator:
    def __init__(self):
        self.equation_first = ""
        self.equation_last = ""
        self.equation_type = ""
        self.current_part = "first"
    
    def input_button(self, button: str):
        if button.isdigit():
            self.add_digit(button)
        elif button in set(item.value for item in Operator):
            self.set_operator(button)
        elif button == EQ_SIGN:
            if self.current_part == "last":
                self.solve()
        elif button == DECIMAL:
            self.add_decimal()
        elif button == FLIP_SIGN:
            self.flip_sign()
        elif button == ALL_CLEAR:
            self.all_clear()
        elif button == CLEAR_ENTRY:
            self.clear_entry()
    
    def set_equation(self, first_part: str | float| int, operator: Operator = None, second_part: str | float | int = ""):
        self.equation_first = str(first_part)
        self.equation_type = operator or ""
        self.equation_last = str(second_part)
        if operator == None:
            self.current_part = "first"
        else:
            self.current_part = "last"
    
    def clear_entry(self):
        if self.current_part == "first":
            self.equation_first = self.equation_first[:-1]
        elif self.current_part == "last":
            if self.equation_last == "":
                self.equation_type = ""
                self.current_part = "first"
            else:
                self.equation_last = self.equation_last[:-1]
    
    def all_clear(self):
        self.set_equation("")

    def add_digit(self, digit):
        if self.current_part == "first":
            self.equation_first += digit
        elif self.current_part == "last":
            self.equation_last += digit

    def set_operator(self, operator: Operator):
        self.equation_type = operator
        self.current_part = "last"
    
    def flip_sign(self):
        if self.current_part == "first":
            if self.equation_first.startswith("-"):
                self.equation_first = self.equation_first.removeprefix("-")
            else:
                self.equation_first = "-" + self.equation_first
        elif self.current_part == "last":
            if self.equation_last.startswith("-"):
                self.equation_last = self.equation_last.removeprefix("-")
            else:
                self.equation_last = "-" + self.equation_last
    
    def add_decimal(self):
        if self.current_part == "first":
            if not "." in self.equation_first:
                self.equation_first += "."
        if self.current_part == "last":
            if not "." in self.equation_last:
                self.equation_last += "."

    def solve(self):
        result = float(self.equation_first)
        
        if self.equation_type == "+":
            result += float(self.equation_last)
        elif self.equation_type == "-":
            result -= float(self.equation_last)
        elif self.equation_type == "/":
            result /= float(self.equation_last)
        elif self.equation_type == "x":
            result *= float(self.equation_last)
        
        if result == int(result):
            self.equation_first = str(int(result))
        else:
            self.equation_first = str(result)

        self.equation_last = ""
        self.equation_type = "" 
        self.current_part = "first"