def add_dots(string: str) -> str:
    return ".".join(string)

    # return "".join(
    #     [
    #         char + "." if index != len(string) - 1 else char
    #         for index, char in enumerate(string)
    #     ]
    # )


def remove_dots(string: str) -> str:
    return string.replace(".", "")
    # return "".join([char for char in string if char != "."])


def tests() -> None:
    print(add_dots("test"))
    print(remove_dots(add_dots("test")))


if __name__ == "__main__":
    tests()
