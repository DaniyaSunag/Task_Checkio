"""Вы должны разделить данный массив на два массива. Если в нем нечетное количество элементов, то в первом массиве должно быть больше элементов.
Если в нем нет элементов, то должны быть возвращены два пустых массива.
Входные данные: Массив.
Вывод: Массив или два массива."""

def split_list(items: list) -> list:
    if len(items) % 2 == 0:
        return [[items[i] for i in range(len(items) // 2)], [items[i] for i in range(len(items) // 2, len(items))]]
    elif len(items) == 1:
        return [[items[0]], []]
    elif len(items) == 0:
        return [[], []]
    else:
        return [[items[i] for i in range(len(items) // 2 + 1)], [items[i] for i in range(len(items) // 2 + 1, len(items))]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")