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
        """Accepts a string input and calls the appropriate function on the calculator."""
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
        """Sets the current equation of the calculator.
        
        >>> calc = Calculator()
        >>> calc.set_equation(2, Operator.MULTIPLY, 2)
        >>> calc.get_equation()
        2 x 2
        """
        self.equation_first = str(first_part)
        self.equation_type = operator or ""
        self.equation_last = str(second_part)
        if operator == None:
            self.current_part = "first"
        else:
            self.current_part = "last"
    
    
    def get_equation(self):
        """Returns the current equation as a single line string.
        
        >>> calc = Calculator()
        >>> calc.set_equation(2, Operator.MULTIPLY, 2)
        >>> calc.get_equation()
        2 x 2
        """
        eq = " ".join([self.equation_first, self.equation_type, self.equation_last])
        eq = eq.rstrip()
        return eq
    
    
    def clear_entry(self):
        """Removes the last entry from the calculator. This could be a digit or the current operator.
        
        >>> calc = Calculator()
        >>> calc.set_equation(2, Operator.MULTIPLY, 2)
        >>> calc.clear_entry()
        >>> calc.clear_entry()
        2
        """
        if self.current_part == "first":
            self.equation_first = self.equation_first[:-1]
        elif self.current_part == "last":
            if self.equation_last == "":
                self.equation_type = ""
                self.current_part = "first"
            else:
                self.equation_last = self.equation_last[:-1]
    
    
    def all_clear(self):
        """Resets the state of the calculator. This is the same as calling self.set_equation('')."""
        self.set_equation("")

    
    def add_digit(self, digit: str | int):
        """Adds a digit to the current number. Accepts str and int.
        
        >>> calc = Calculator()
        >>> calc.add_digit('2')
        >>> calc.add_digit(4)
        >>> calc.get_equation()
        24
        """
        if self.current_part == "first":
            self.equation_first += str(digit)
        elif self.current_part == "last":
            self.equation_last += str(digit)

    
    def set_operator(self, operator: Operator):
        """Sets the operator of the equation. Also changes the current number to the second one.
        
        >>> calc = Calculator()
        >>> calc.add_digit(2)
        >>> calc.set_operator(Operator.ADD)
        >>> calc.add_digit(4)
        >>> calc.set_operator(Operator.SUB)
        >>> calc.get_equation()
        2 - 4
        """
        self.equation_type = operator
        self.current_part = "last"
    
    
    def flip_sign(self):
        """Flips the sign of the current number.
        
        >>> calc = Calculator()
        >>> calc.add_digit(2)
        >>> calc.flip_sign()
        >>> calc.get_equation()
        -2

        >>> calc = Calculator()
        >>> calc.set_equation(-2)
        >>> calc.flip_sign()
        >>> calc.get_equation()
        2
        """
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
        """Adds a decimal to the end of the current number if it doesn't have one. Otherwise it does nothing.
        
        >>> calc = Calculator()
        >>> calc.add_digit(2)
        >>> calc.add_decimal()
        >>> calc.add_digit(5)
        >>> calc.get_equation()
        2.5
        """
        if self.current_part == "first":
            if not "." in self.equation_first:
                self.equation_first += "."
        if self.current_part == "last":
            if not "." in self.equation_last:
                self.equation_last += "."

    
    def solve(self):
        """Solves the equation currently stored in the calculator and sets the equation to the new result.
        
        >>> calc = Calculator()
        >>> calc.set_equation(1, Operator.ADD, 1)
        >>> calc.solve()
        >>> calc.get_equation()
        2
        """
        result = float(self.equation_first)
        
        if self.equation_type == Operator.ADD:
            result += float(self.equation_last)
        elif self.equation_type == Operator.SUBTRACT:
            result -= float(self.equation_last)
        elif self.equation_type == Operator.DIVIDE:
            result /= float(self.equation_last)
        elif self.equation_type == Operator.MULTIPLY:
            result *= float(self.equation_last)
        
        if result == int(result):
            self.equation_first = str(int(result))
        else:
            self.equation_first = str(result)

        self.equation_last = ""
        self.equation_type = "" 
        self.current_part = "first"