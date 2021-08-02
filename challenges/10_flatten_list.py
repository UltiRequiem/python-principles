def flatten(lst_of_lst: list) -> list:
    return [item for sublist in lst_of_lst for item in sublist]


def tests() -> None:
    print(flatten([[1, 2], [3, 4], [5, 6]]))
    print(flatten([[1, 4], [5, 4], [5, 6]]))


if __name__ == "__main__":
    tests()
