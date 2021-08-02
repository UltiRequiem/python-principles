"""
Define a function named triple_and that takes three parameters
and returns True only if they are all True and False otherwise.
"""


def triple_and(one: bool, two: bool, three: bool) -> bool:
    return one and two and three


def test() -> None:
    print(triple_and(True, False, True))
    print(triple_and(True, True, True))
    print(triple_and(False, False, False))


if __name__ == "__main__":
    test()
