import pytest
from utils.calculator import add

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_with_negative_numbers():
    assert divide(-10, 5) == -2
    assert divide(10, -5) == -2
    assert divide(-10, -5) == 2

def test_divide_floating_point():
    result = divide(1, 3)
    assert abs(result - 0.3333333333333333) < 1e-9

def test_divide_large_numbers():
    assert divide(1e308, 1e307) == 10

def test_divide_small_numbers():
    assert divide(1e-308, 1e-309) == pytest.approx(10, rel=1e-15)

def test_divide_large_and_small_numbers():
    assert divide(1e308, 1e-308) == 1e616
