"""
Your function should return True if both parameters are integers, and False otherwise.
"""


def only_ints(a, b) -> bool:
    return type(a) == int and type(b) == int


def tests() -> None:
    print(only_ints(4, 8))
    print(only_ints(4, "u"))
    print(only_ints("a", 4))
    print(only_ints(4, True))


if __name__ == "__main__":
    tests()
