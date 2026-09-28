"""Tests for calculator operations."""

import pytest

from app.operation import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),
        (-2, 2, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 4, 6),
        (5, 10, -5),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtract(a, b, expected):
    assert Subtract().execute(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 15),
        (-2, 4, -8),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert Multiply().execute(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (5, 2, 2.5),
        (-10, 2, -5),
    ],
)
def test_divide(a, b, expected):
    assert Divide().execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Divide().execute(10, 0)