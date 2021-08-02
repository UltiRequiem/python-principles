"""
The built-in zip function "zips" two lists.
Write your own implementation of this function.
"""


def zap(a: list, b: list) -> list:
    return [(a[i], b[i]) for i in range(len(a))]


def test() -> None:
    print(zap([0, 1, 2, 3], [5, 6, 7, 8]))


if __name__ == "__main__":
    test()
