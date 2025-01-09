import pytest
from utils.calculator import add, divide, multiply, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 0) == 10
    assert subtract(0, 10) == -10

def test_multiply():
    # Case 1: Multiply two positive numbers
    assert multiply(3, 4) == 12

    # Case 2: Multiply two negative numbers
    assert multiply(-2, -5) == 10

    # Case 3: Multiply a positive and a negative number
    assert multiply(6, -7) == -42

    # Case 4: Multiply by zero (result should always be 0)
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0

    # Case 5: Multiply two zeros
    assert multiply(0, 0) == 0

def test_divide():
    # Test division of integers
    assert divide(10, 2) == 5
    # Test division resulting in a floating-point number
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    # Attempting to divide by zero should raise a ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
