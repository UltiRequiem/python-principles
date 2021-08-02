def count(word: str) -> int:
    return word.count("-") + 1
    # return len(word.split("-"))


def tests() -> None:
    print(count("ho-tel"))
    print(count("ca-sa"))


if __name__ == "__main__":
    tests()
