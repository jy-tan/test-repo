import pytest
from utils.calculator import add, divide

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_large_numbers():
    large_num = 1e308
    small_num = 1e-308
    assert divide(large_num, 1) == large_num
    assert divide(1, large_num) == 1e-308
    assert divide(small_num, 1) == small_num
    assert divide(1, small_num) == 1e308

def test_divide_with_negative_numbers():
    assert divide(-10, 5) == -2
    assert divide(10, -5) == -2
    assert divide(-10, -5) == 2

def test_divide_floating_point_precision():
    assert divide(1, 3) == pytest.approx(0.3333333333333333, rel=1e-9)
    assert divide(2, 3) == pytest.approx(0.6666666666666666, rel=1e-9)
    assert divide(10, 3) == pytest.approx(3.3333333333333335, rel=1e-9)

