def count_ocurrences(data: dict, word: str | int) -> int:
    return sum(value == word for value in data.values())
    # return len([p for p in statuses if statuses[p] == word])


def test() -> None:
    STATUSES = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
        "Eve Two": "online",
    }

    print(count_ocurrences(STATUSES, 2))


if __name__ == "__main__":
    test()
