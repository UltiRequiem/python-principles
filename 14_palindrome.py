def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def tests() -> None:
    print(is_palindrome("bob"))
    print(is_palindrome("ana"))
    print(is_palindrome("pedro"))


if __name__ == "__main__":
    tests()
