from __future__ import annotations


from typing import Any


NAME_DEFAULT = 'Unit'
DAMAGE_DEFAULT = 5
HIT_POINT_DEFAULT = 10
HIT_POINT_LIMIT_DEFAULT = 10


def _is_int(value: Any) -> int:
    return int(value)


def _is_string(value: Any) -> str:
    if type(value) == str:
        return str(value)
    else:
        raise TypeError()


class Unit:
    def __init__(self,
                 name: str = NAME_DEFAULT,
                 damage: int = DAMAGE_DEFAULT,
                 hit_point: int = HIT_POINT_DEFAULT,
                 hit_point_limit: int = HIT_POINT_LIMIT_DEFAULT,
                 ) -> None:
        self._damage = _is_int(damage)
        self._hit_point = _is_int(hit_point)
        self._hit_point_limit = _is_int(hit_point_limit)
        self._name = _is_string(name)

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def hit_point(self) -> int:
        return self._hit_point

    @property
    def hit_point_limit(self) -> int:
        return self._hit_point_limit

    @property
    def name(self) -> str:
        return self._name

    @damage.setter
    def damage(self, value: Any) -> None:
        self._damage = _is_int(value)

    @hit_point.setter
    def hit_point(self, value: Any) -> None:
        self._hit_point = _is_int(value)

    @hit_point_limit.setter
    def hit_point_limit(self, value: Any) -> None:
        self._hit_point_limit = _is_int(value)

    def __str__(self) -> str:
        return f'Name - {self.name}\nHealth - {self.hit_point}\nAttack - {self.damage}'

    def ensure_is_alive(self) -> None:
        if self.hit_point == 0:
            raise Exception(f'I am Dead')

    def take_damage(self, value: Any) -> None:
        if value >= self.hit_point:
            self.hit_point = 0
        else:
            self.hit_point -= value

    def attack(self, enemy: Unit) -> None:
        self.ensure_is_alive()
        enemy.take_damage(self.damage)
        enemy.counter_attack(self)

    def counter_attack(self, attacker: Unit) -> None:
        attacker.ensure_is_alive()
        attacker.take_damage(self.damage/2)
