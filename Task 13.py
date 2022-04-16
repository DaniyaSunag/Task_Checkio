"""Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
Входные данные: Строка.
Выходные данные: Массив строк."""

def split_pairs(a):
    pairs_list = []
    for index in range(0, len(a), 2):
        element = a[index:index+2]
        if len(element) == 1:
            pairs_list.append((element + "_"))
        else:
            pairs_list.append(element)

    return pairs_list


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")