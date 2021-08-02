"""
Your function must return whether n is exclusively in list1 or list2.

In other words, if n is in both lists or in none of the lists,
return False. If n is in only one of the lists, return True.
"""


def list_xor(val, lst_one: list, lst_two: list) -> bool:
    return (val in lst_one) ^ (val in lst_two)


def test() -> None:
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))
    print(list_xor(1, [0, 2, 3], [1, 5, 6]))
    print(list_xor(1, [1, 2, 3], [1, 5, 6]))
    print(list_xor(1, [0, 0, 0], [4, 5, 6]))


if __name__ == "__main__":
    test()
