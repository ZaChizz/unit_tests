import pytest

from src.vector.vector import Vector


VECTOR_DEFAULT = 1.0
VECTOR_NEW_VALUE = 10.0


@pytest.mark.parametrize('params', [
    (), (10.0, 5.0)
])
def test_constructor(params):
    vector = Vector(*params)

    assert vector.x == params[0] if params != () else VECTOR_DEFAULT
    assert vector.y == params[1] if params != () else VECTOR_DEFAULT


@pytest.mark.parametrize('x, y, exception_type', [
    ('asd', 'asd', ValueError), (Vector, Vector, TypeError)
])
def test_constructor_exceptions(x, y, exception_type):
    with pytest.raises(exception_type):
        Vector(x, y)


def test_setters():
    point = Vector()

    assert point.x == VECTOR_DEFAULT
    assert point.y == VECTOR_DEFAULT

    point.x = VECTOR_NEW_VALUE
    point.y = VECTOR_NEW_VALUE

    assert point.x == VECTOR_NEW_VALUE
    assert point.y == VECTOR_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Vector, TypeError)
])
def test_setter_exceptions(value, exception_type):
    vector = Vector()

    with pytest.raises(exception_type):
        vector.x = value


@pytest.mark.parametrize('params, string_repr', [
    ((), '(1.0, 1.0)'), ((10.0, 5.0), '(10.0, 5.0)')
])
def test_string_repr(params, string_repr):
    vector = Vector(*params)

    assert str(vector) == string_repr


def test_comparison_operators():
    p1 = Vector()
    p2 = Vector()
    p3 = Vector(2.0, 4.0)

    assert p1 == p2
    assert not p1 == p3
    assert p1 != p3
    assert not p1 != p2


def test_comparison_operators_exception():
    p1 = Vector()

    with pytest.raises(TypeError):
        p1 == 1234


def test_len():
    p1 = Vector()
    p2 = Vector(2.0, 4.0)

    assert p1.len(p2) == 3.1622776601683795


def test_len_exception():
    with pytest.raises(TypeError):
        Vector().len('Some string')


def test_add():
    p1 = Vector(2.0, 2.0)
    p2 = Vector(2.0, 2.0)

    assert p1 + p2 == Vector(4.0, 4.0)


def test_add_exception():
    with pytest.raises(TypeError):
        Vector() + 'asd'


def test_sub():
    p1 = Vector(3.0, 3.0)
    p2 = Vector(1.0, 1.0)

    assert p1 - p2 == Vector(2.0, 2.0)


def test_sub_exception():
    with pytest.raises(TypeError):
        Vector() - 'asd'
