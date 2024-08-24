import pytest
from app.app import add, subtract, multiply, division


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(2, 1) == 1


def test_multiply():
    assert multiply(2, 3) == 6


def test_division():
    assert division(2, 1) == 2
    assert division(2, 0) == "Division by zero is not allowed"
