import pytest

from src.generators.generators import ari_prog, geo_prog, fibonacci, factorial


def test_ari_prog():
    generator = ari_prog(0, 10, 2)
    expected_results = [0, 2, 4, 6, 8]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_geo_prog():
    generator = geo_prog(1, 10, 2)
    expected_results = [1, 2, 4, 8]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_factorial():
    generator = factorial(5)
    expected_results = [1, 2, 6, 24, 120]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_fibonacci():
    generator = fibonacci(5)
    expected_results = [0, 1, 1, 2, 3, 5]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)