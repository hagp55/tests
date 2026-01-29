import pytest


@pytest.mark.parametrize(
    "p1,p2,expected, ",
    [
        (1, 2, 3),
        (10, 7, 17),
        (15, 10, 25),
    ],
)
def test_sum(p1, p2, expected):
    assert p1 + p2 == expected


def test_eq():
    assert 1 == 1


def test_div():
    assert 10 / 2 == 5
