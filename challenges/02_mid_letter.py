def mid(word: str | list | tuple) -> str:
    return "" if len(word) % 2 == 0 else word[round(len(word) // 2)]


def tests() -> None:
    print(mid("hello"))  # "l"
    print(mid("12345"))  # "3"
    print(mid("hello2"))  # ""
    print(mid("abc"))  # "b"
    # It also works with lists!
    print(mid(["a", "b", "c", "d", "e"]))  # "c"
    print(mid(("1", "2", "3", "4", "5")))  # "3"


if __name__ == "__main__":
    tests()
