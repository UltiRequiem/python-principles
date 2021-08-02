def largest_difference(lst: list[int]):
    return max(lst) - min(lst)


def test() -> None:
    print(largest_difference([34, 22, 55]))


if __name__ == "__main__":
    test()
