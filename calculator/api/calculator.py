class Calculator:
    def __init__(self):
        self.equation_first = ""
        self.equation_last = ""
        self.equation_type = ""
        self.current_part = "first"
    
    def input_button(self, button: str):
        if button.isdigit():
            self.add_digit(button)
        elif button in ["+", "-", "/", "x"]:
            self.set_operator(button)
        elif button == "=":
            if self.current_part == "last":
                self.solve()
        elif button == ".":
            self.add_decimal()
        elif button == "+/-":
            self.flip_sign()
    
    def add_digit(self, digit):
        if self.current_part == "first":
            self.equation_first += digit
        elif self.current_part == "last":
            self.equation_last += digit

    def set_operator(self, operator):
        self.equation_type = operator
        if self.current_part == "first":
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