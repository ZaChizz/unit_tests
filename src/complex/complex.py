from __future__ import annotations


from typing import Any


def _validate(value: Any) -> float:
    return float(value)


class Complex:
    def __init__(self, real: float = 1.0, imaginary: float = 1.0) -> None:
        self._real = _validate(real)
        self._imaginary = _validate(imaginary)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead.'
            )

    @property
    def real(self) -> float:
        return self._real

    @property
    def imaginary(self) -> float:
        return self._imaginary

    @real.setter
    def real(self, value: Any) -> None:
        self._real = _validate(value)

    @imaginary.setter
    def imaginary(self, value: Any) -> None:
        self._imaginary = _validate(value)

    def __str__(self) -> str:
        if self._imaginary == 0:
            return f'{self.real}'
        if self._imaginary < 0:
            self._imaginary *= -1
            return f'{self.real} - {self.imaginary}i'
        else:
            return f'{self.real} + {self.imaginary}i'

    def __eq__(self, other: Complex) -> bool:
        self._check_type(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other: Complex) -> bool:
        return not self == other

    def __add__(self, other: Complex) -> Complex:
        self._check_type(other)
        return Complex(self._real + other.real, self._imaginary + other.imaginary)

    def __sub__(self, other: Complex) -> Complex:
        self._check_type(other)
        return Complex(self._real - other.real, self._imaginary - other.imaginary)

    def __mul__(self, other: Any) -> Complex:
        if not (type(other) == int or type(other) == float):
            self._check_type(other)
            return Complex(self._real * other.real - self._imaginary * other.imaginary,
                           self.real * other.imaginary + self._imaginary * other.real)
        else:
            return Complex(self._real * other, self._imaginary * other)
