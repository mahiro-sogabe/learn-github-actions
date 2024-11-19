from src import calc


def test_calc_1() -> None:
    """足し算 正常系"""
    a: int = 3
    b: int = 4
    total_value: int = a + b

    assert calc.calc(a, b) == total_value


def test_calc_2() -> None:
    """足し算 正常系"""
    a: int = 3
    b: int = 4
    total_value: int = 9

    assert calc.calc(a, b) == total_value
