from typing import Any
from typing import Generator


def ari_prog(start, stop, step):
    while start < stop:
        yield start

        start += step


def geo_prog(start, stop, q):
    while start < stop:
        yield start

        start *= q


def factorial(y: int):
    a = 1
    for j in range(1, y+1):
        a *= j
        yield a


def fibonacci(n: int) -> Generator[int, Any, None]:
    fib1 = -1
    fib2 = 1
    i = 0
    while i <= n:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        yield fib2


if __name__ == '__main__':  # pragma: no cover
    for i in ari_prog(0, 10, 2):
        print(i)
    for i in geo_prog(1, 10, 2):
        print(i)
    for i in factorial(5):
        print(i)
    for i in fibonacci(5):
        print(i)

