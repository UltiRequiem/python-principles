def consecutive(string: str, separetor: str = "1") -> int:
    return max([len(c) for c in string.split(separetor)])


def test() -> None:
    print(consecutive("1001101000110"))


if __name__ == "__main__":
    test()
