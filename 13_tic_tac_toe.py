def get_row_col(string: str) -> tuple:
    return (int(string[1]) - 1, {"A": 0, "B": 1, "C": 2}[string[0]])


def test() -> None:
    print(get_row_col("C1"))


if __name__ == "__main__":
    test()
