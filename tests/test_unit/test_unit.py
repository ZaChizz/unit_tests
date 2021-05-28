import pytest

from src.unit.unit import Unit


NAME_DEFAULT = 'Unit'
DAMAGE_DEFAULT = 5
HIT_POINT_DEFAULT = 10
HIT_POINT_LIMIT_DEFAULT = 10

DAMAGE_NEW = 10
HIT_POINT_NEW = 20
HIT_POINT_LIMIT_NEW = 20


@pytest.mark.parametrize('params', [
    (), ('b', 5, 10, 10),
])
def test_constructor(params):
    unit1 = Unit(*params)

    assert unit1.name == params[0] if params != () else NAME_DEFAULT
    assert unit1.damage == params[1] if params != () else DAMAGE_DEFAULT
    assert unit1.hit_point == params[2] if params != () else HIT_POINT_DEFAULT
    assert unit1.hit_point_limit == params[3] if params != () else HIT_POINT_LIMIT_DEFAULT


@pytest.mark.parametrize('name, damage, hit_point, hit_point_limit, exception_type', [
    ('name', 'str', 12, 12, ValueError),
    ('name', 12, 'str', 12, ValueError),
    ('name', 12, 12, 'str', ValueError),
    (Unit, 12, 12, 12, TypeError),
    ('name', Unit, 12, 12, TypeError),
    ('name', 12, Unit, 12, TypeError),
    ('name', 12, 12, Unit, TypeError)
])
def test_constructor_exception(name, damage, hit_point, hit_point_limit, exception_type):
    with pytest.raises(exception_type):
        Unit(name, damage, hit_point, hit_point_limit)


def test_setters():
    unit1 = Unit()

    assert unit1.name == NAME_DEFAULT
    assert unit1.damage == DAMAGE_DEFAULT
    assert unit1.hit_point == HIT_POINT_DEFAULT
    assert unit1.hit_point_limit == HIT_POINT_LIMIT_DEFAULT

    unit1.damage = DAMAGE_NEW
    unit1.hit_point = HIT_POINT_NEW
    unit1.hit_point_limit = HIT_POINT_LIMIT_NEW

    assert unit1.damage == DAMAGE_NEW
    assert unit1.hit_point == HIT_POINT_NEW
    assert unit1.hit_point_limit == HIT_POINT_LIMIT_NEW


@pytest.mark.parametrize('value, exception_type', [
    ('str', ValueError), (Unit, TypeError)
])
def test_setters_exception(value, exception_type):
    unit1 = Unit()

    with pytest.raises(exception_type):
        unit1.damage = value
        unit1.hit_point = value
        unit1.hit_point_limit = value


@pytest.mark.parametrize('params, string_repr', [
    ((), 'Name - Unit\nHealth - 10\nAttack - 5'),
    (('Soldier', 12, 12, 12), 'Name - Soldier\nHealth - 12\nAttack - 12'),
])
def test_string_repr(params, string_repr):
    unit1 = Unit(*params)

    assert str(unit1) == string_repr


def test_ensure_is_alive():
    unit1 = Unit()
    unit1.hit_point = 0

    with pytest.raises(Exception):
        unit1.ensure_is_alive()


def test_attack():
    unit1 = Unit()
    unit2 = Unit()

    unit1.attack(unit2)

    assert unit1.name == NAME_DEFAULT
    assert unit1.damage == DAMAGE_DEFAULT
    assert unit1.hit_point == 7
    assert unit1.hit_point_limit == HIT_POINT_LIMIT_DEFAULT

    assert unit2.name == NAME_DEFAULT
    assert unit2.damage == DAMAGE_DEFAULT
    assert unit2.hit_point == 5
    assert unit2.hit_point_limit == HIT_POINT_LIMIT_DEFAULT

    unit1.attack(unit2)

    assert unit1.name == NAME_DEFAULT
    assert unit1.damage == DAMAGE_DEFAULT
    assert unit1.hit_point == 4
    assert unit1.hit_point_limit == HIT_POINT_LIMIT_DEFAULT

    assert unit2.name == NAME_DEFAULT
    assert unit2.damage == DAMAGE_DEFAULT
    assert unit2.hit_point == 0
    assert unit2.hit_point_limit == HIT_POINT_LIMIT_DEFAULT
