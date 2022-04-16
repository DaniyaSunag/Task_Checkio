"""В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.
Входные данные: Список.
Выходные данные: Набор элементов."""

from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        replaced_items = items[1:]
        replaced_items.append(items[0])
        return replaced_items
    return items


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")