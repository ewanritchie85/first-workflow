from src.adder import adder


def test_adder_returns_int():
    result = adder(1, 2)
    assert isinstance(result, int)

def test_adder_returns_sum():
    result = adder(1, 2)
    assert result == 3