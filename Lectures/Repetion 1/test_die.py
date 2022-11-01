import pytest

from die import Die


def test_init_value():
    expected = 5
    d = Die(expected)
    assert d.value == expected


def test_init_no_value():
    expected = None
    d = Die()
    assert d.value == expected


def test_roll():
    d = Die()
    assert d.value is None
    d.roll()
    assert d.value is not None
    assert 1 <= d.value <= 6


if __name__ == '__main__':
    pytest.main()
