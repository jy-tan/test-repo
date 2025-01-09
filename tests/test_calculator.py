import pytest
from utils.calculator import add, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_multiply_positive_integers():
    result = multiply(3, 4)
    assert result == 12

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

