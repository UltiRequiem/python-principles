"""
Define a function param_count that takes a variable number of parameters.
The function should return the number of arguments it was called with.
"""


def param_count(*args):
    return len(args)


def test() -> None:
    print(param_count())
    print(param_count(1, 2))


if __name__ == "__main__":
    test()
