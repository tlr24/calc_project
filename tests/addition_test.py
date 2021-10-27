"""Test addition"""
from calculator.operations.addition import Addition


def test_addition():
    """Testing calc result is 3"""
    assert Addition.add(1, 2) == 3
