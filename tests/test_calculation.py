"""Tests for calculations and the CalculationFactory."""

import pytest

from app.calculation import CalculationFactory


@pytest.mark.parametrize(
    "operation, a, b, expected",
    [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 5, 3, 15),
        ("divide", 10, 2, 5),
    ],
)
def test_calculation_factory(operation, a, b, expected):
    calculation = CalculationFactory.create_calculation(operation, a, b)
    assert calculation.perform() == expected


def test_factory_accepts_uppercase():
    calculation = CalculationFactory.create_calculation("ADD", 5, 3)
    assert calculation.perform() == 8


def test_invalid_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create_calculation("power", 5, 2)


def test_calculation_string():
    calculation = CalculationFactory.create_calculation("add", 5.0, 3.0)
    assert str(calculation) == "AddCalculation: 5.0 Add 3.0 = 8.0"


def test_calculation_divide_by_zero():
    calculation = CalculationFactory.create_calculation("divide", 10, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculation.perform()