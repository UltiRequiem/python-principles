"""
Define a function named convert that takes a list of numbers as its 
only parameter and returns a list of each number converted to a string.
"""


def convert(lst: list):
    return [str(n) for n in lst]
    # return list(map(str, lst))


def test() -> None:
    print(convert([1, 2, 3, 4]))


if __name__ == "__main__":
    test()
