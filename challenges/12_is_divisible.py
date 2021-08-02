def if_divisible(num, div=3):
    return num % div == 0


def test() -> None:
    print(if_divisible(3))
    print(if_divisible(50, 50))


if __name__ == "__main__":
    test()
