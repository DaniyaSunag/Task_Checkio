"""У вас есть последовательность строк, и вы хотели бы определить наиболее часто встречающуюся строку в этой последовательности. Он может быть только один.
Ввод: непустой список строк.
Вывод: строка."""
def most_frequent(data: list) -> str:
    max_num = max([data.count(element) for element in data])
    for sym in data:
        if data.count(sym) == max_num:
            return sym


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")