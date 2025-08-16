import pytest
from calculator.api import *

@pytest.mark.parametrize("test_input,expected", [
    ([1], "1"),
    (["1"], "1"),
    ([1, Operator.ADD, 1], "1 + 1"),
    (["1", Operator.ADD, "1"], "1 + 1"),
    ([1, Operator.SUBTRACT], "1 -"),
    ([1, Operator.DIVIDE], "1 /"),
    ([1, Operator.MULTIPLY], "1 x"),
    ([2.6, Operator.ADD, 1.4], "2.6 + 1.4")
])
def test_get_set_equation(test_input, expected):
    calc = Calculator()
    calc.set_equation(*test_input)
    assert calc.get_equation() == expected

@pytest.mark.parametrize("test_input,expected", [
    ([1, Operator.ADD, 1], "2"),
    ([1, Operator.SUBTRACT, 2], "-1"),
    ([1, Operator.DIVIDE, 2], "0.5"),
    ([2, Operator.MULTIPLY, 4], "8")
])
def test_solve_equation(test_input, expected):
    calc = Calculator()
    calc.set_equation(*test_input)
    calc.solve()
    assert calc.get_equation() == expected

@pytest.mark.parametrize("test_input,expected", [
    (1, "-1"),
    (-1, "1"),
    ("1", "-1"),
    ("-1", "1")
])
def test_flip_sign(test_input, expected):
    calc = Calculator()
    calc.set_equation(test_input)
    calc.flip_sign()
    assert calc.get_equation() == expected