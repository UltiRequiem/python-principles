def format_thousands(n: int) -> str:
    """Format Numbers"""
    return f"{n:,}"


def test() -> None:
    print(format_thousands(10000000))


if __name__ == "__main__":
    test()
