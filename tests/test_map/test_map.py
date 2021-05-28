import pytest
from map import increment, pow2, sequence_handler


@pytest.mark.parametrize('value, result', [
    (10, 11), (-7, -6)
])
def test_increment(value, result):
    assert increment(value) == result


@pytest.mark.parametrize('value, result', [
    (0, 0), (1, 1), (5, 25)
])
def test_pow2(value, result):
    assert pow2(value) == result


def test_sh():
    assert sequence_handler(increment, [1, 2, 3]) == [2, 3, 4]
