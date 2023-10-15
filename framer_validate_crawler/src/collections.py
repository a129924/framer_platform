from typing import Iterable, TypeVar

T = TypeVar("T")


def unpack(iterable: Iterable[list[T]]) -> list[T]:
    from itertools import chain

    return list(chain.from_iterable(iterable))


if __name__ == "__main__":
    matrix = ([1, 2, 3], [4, 5, 6])

    print(unpack(matrix))
