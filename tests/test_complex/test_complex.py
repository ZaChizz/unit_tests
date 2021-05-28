import pytest

from src.complex.complex import Complex


COMPLEX_DEFAULT = 1.0
COMPLEX_NEW_VALUE = 10.0


@pytest.mark.parametrize('params', [
    (), (10.0, 5.0)
])
def test_constructor(params):
    complex1 = Complex(*params)

    assert complex1.real == params[0] if params != () else COMPLEX_DEFAULT
    assert complex1.imaginary == params[1] if params != () else COMPLEX_DEFAULT


@pytest.mark.parametrize('real, imaginary, exception_type', [
    ('asd', 'asd', ValueError), (Complex, Complex, TypeError)
])
def test_constructor_exceptions(real, imaginary, exception_type):
    with pytest.raises(exception_type):
        Complex(real, imaginary)


def test_setters():
    complex1 = Complex()

    assert complex1.real == COMPLEX_DEFAULT
    assert complex1.imaginary == COMPLEX_DEFAULT

    complex1.real = COMPLEX_NEW_VALUE
    complex1.imaginary = COMPLEX_NEW_VALUE

    assert complex1.real == COMPLEX_NEW_VALUE
    assert complex1.imaginary == COMPLEX_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Complex, TypeError)
])
def test_setter_exceptions(value, exception_type):
    complex1 = Complex()

    with pytest.raises(exception_type):
        complex1.real = value


@pytest.mark.parametrize('params, string_repr', [
    ((), '1.0 + 1.0i'), ((10.0, 5.0), '10.0 + 5.0i'), ((1.0, 0), '1.0'), ((1.0, -5), '1.0 - 5.0i')
])
def test_string_repr(params, string_repr):
    complex1 = Complex(*params)

    assert str(complex1) == string_repr


def test_comparison_operators():
    p1 = Complex()
    p2 = Complex()
    p3 = Complex(2.0, 4.0)

    assert p1 == p2
    assert not p1 == p3
    assert p1 != p3
    assert not p1 != p2


def test_comparison_operators_exception():
    p1 = Complex()

    with pytest.raises(TypeError):
        p1 == 1234


def test_add():
    p1 = Complex(2.0, 2.0)
    p2 = Complex(2.0, 2.0)

    assert p1 + p2 == Complex(4.0, 4.0)


def test_add_exception():
    with pytest.raises(TypeError):
        Complex() + 'asd'


def test_sub():
    p1 = Complex(3.0, 3.0)
    p2 = Complex(1.0, 1.0)

    assert p1 - p2 == Complex(2.0, 2.0)


def test_sub_exception():
    with pytest.raises(TypeError):
        Complex() - 'asd'


def test_mull():
    p1 = Complex(2, 3)
    p2 = Complex(-1, 1)

    assert p1 * p2 == Complex(-5, -1)
    assert p1 * 2 == Complex(4, 6)
