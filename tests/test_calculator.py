import pytest
from utils.calculator import add

def test_add():
    assert add(1, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
