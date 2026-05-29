from add_calculator import add


def test_adds_two_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_adds_negative_numbers() -> None:
    assert add(-2, -3) == -5


def test_adds_decimal_numbers() -> None:
    assert add(1.5, 2.25) == 3.75
