import pytest
from utils.calculator import add, multiply, divide, sqrt

def test_add():
    assert add(1, 2) == 3

def test_multiply_positive_integers():
    result = multiply(3, 4)
    assert result == 12

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_sqrt_positive_float():
    input_value = 2.25
    expected_output = 1.5
    assert sqrt(input_value) == expected_output

def test_sqrt_negative_number():
    result = sqrt(-1)
    assert isinstance(result, complex), "The result should be a complex number for negative inputs."
    assert result.imag != 0, "The imaginary part of the result should be non-zero for negative inputs."

