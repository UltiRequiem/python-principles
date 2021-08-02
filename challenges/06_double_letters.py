"""
Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""


def double_letters(string: str) -> bool:
    return any((a == b for a, b in zip(string, string[1:])))


def tests() -> None:
    print(double_letters("hello"))
    print(double_letters("nono"))


if __name__ == "__main__":
    tests()
