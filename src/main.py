from point.point import Point
from vector.vector import Vector
from complex.complex import Complex
from unit.unit import Unit

if __name__ == '__main__':
    point = Point()
    point2 = Point(7, 2)
    print(point2)
    vector1 = Vector()
    vector2 = Vector(1, 2)
    vector3 = vector1 + vector2
    vector4 = vector1 - vector2
    vector3 += vector2
    print(vector3)
    complex1 = Complex(2, 3)
    complex2 = Complex(-1, 1)

    print(complex1 * complex2)
    print(complex1 * 3.0)
    print(complex1 * 2)

    vasy = Unit('Vasy')
    pety = Unit('Pety')
    print(vasy)
    print('\n')
    print(pety)
    print('--Fight--')
    vasy.attack(pety)
    print(vasy)
    print('\n')
    print(pety)

