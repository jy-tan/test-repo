import pytest
import math
from utils.calculator import add, multiply, divide, sqrt, log

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
    # Test that log returns the natural logarithm of a positive number
    # Using a value with a known logarithm for precise verification
    test_value = 2.718281828459045  # Approximately e
    expected_result = 1.0  # log(e) = 1
    
    result = log(test_value)
    
    # Using pytest.approx for floating-point comparison to handle small precision differences
    assert result == pytest.approx(expected_result)

def test_log_of_one():
    # Test that log(1) returns 0, which is a fundamental mathematical property
    result = log(1)
    
    # Using pytest.approx for floating-point comparison to handle small precision differences
    assert result == pytest.approx(0)

def test_log_negative_number():
    # Test that log raises a ValueError when called with a negative number
    with pytest.raises(ValueError):
        log(-1)

def test_log_zero():
    # Test that log raises a ValueError when called with zero
    with pytest.raises(ValueError):
        log(0)

def test_log_very_large_number():
    # Test that log handles very large positive numbers correctly
    test_value = 1e100  # 10^100
    
    # Expected result: log(10^100) = 100 * log(10)
    expected_result = 100 * math.log(10)
    
    result = log(test_value)
    
    # Using pytest.approx for floating-point comparison
    assert result == pytest.approx(expected_result)
