import pytest
from utils.calculator import add, multiply, divide, sqrt, log, tan

def test_add():
    assert add(1, 2) == 3

def test_multiply_positive_integers():
    result = multiply(3, 4)
    assert result == 12

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_sqrt_positive_number():
    assert sqrt(4) == 2

def test_sqrt_zero():
    assert sqrt(0) == 0

def test_log_positive_number():
    # Test with a value close to e (2.718...) which should give a result close to 1
    result = log(2.718)
    # Using pytest's approx for floating-point comparison
    assert result == pytest.approx(1.0, abs=1e-3)
    
    # Test with another positive number
    result = log(10)
    assert result == pytest.approx(2.302585, abs=1e-6)

def test_log_of_one():
    """Test that log(1) returns 0, which is a fundamental property of logarithms."""
    result = log(1)
    assert result == pytest.approx(0.0)

def test_log_negative_number():
    # The natural logarithm is only defined for positive real numbers
    # When given a negative number, math.log() raises a ValueError
    with pytest.raises(ValueError):
        log(-1)

def test_log_zero():
    """Test that log(0) raises a ValueError as expected."""
    with pytest.raises(ValueError):
        log(0)

def test_log_non_numeric_input():
    # Test with a string
    with pytest.raises(TypeError):
        log("not a number")
    
    # Test with a list
    with pytest.raises(TypeError):
        log([1, 2, 3])
    
    # Test with a dictionary
    with pytest.raises(TypeError):
        log({"key": "value"})
    
    # Test with None
    with pytest.raises(TypeError):
        log(None)
