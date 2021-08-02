def is_anagram(one: str, two: str):
    return sorted(one) == sorted(two)


def test() -> None:
    print(is_anagram("typhoon", "opython"))
    print(is_anagram("letras", "lastre"))
    print(is_anagram("Alice", "Bob"))


if __name__ == "__main__":
    test()
