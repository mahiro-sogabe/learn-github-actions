import pytest

from src import calc


def test_calc_1():
    a: int = 3
    b: int = 4
    sum = a + b

    assert calc.calc(a, b) == sum
