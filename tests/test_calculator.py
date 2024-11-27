import pytest
from utils.calculator import add, divide, multiply

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(10, 5) == 2

def test_multiply():
    assert multiply(2, 3) == 6
