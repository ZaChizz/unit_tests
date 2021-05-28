from typing import Callable


def increment(x: int) -> int:
    return x + 1


def pow2(x: int) -> int:
    return x ** 2


def sequence_handler(func: Callable, sequence: list) -> list:
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


if __name__ == '__main__':  # pragma: no cover
    source = [1, 2, 3, 4, 5]

    print(source)
    print(sequence_handler(increment, source))
    print(sequence_handler(pow2, source))

    print()
    print(sequence_handler(lambda x: x + 1, source))
    print(sequence_handler(lambda x: x ** 2, source))

    print()
    print(list(map(lambda x: x + 1, source)))
    print(list(map(lambda x: x ** 2, source)))
