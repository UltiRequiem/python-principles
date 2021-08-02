import random


def random_number():
    # return random.choice(range(1, 101))
    return random.randint(1, 100)


def test() -> None:
    print(random_number())


if __name__ == "__main__":
    test()
