import pytest
from app.app import add, subtract, division

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_division():
    assert division(2,1) == 2