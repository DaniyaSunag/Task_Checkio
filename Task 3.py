"""Вы начали серию задач связаную с паролями. Каждая следующая задача связана с предыдущей. Каждая следующая задача будет сложнее предыдущей.
В этой задаче, Вам нужно создать функцию проверки пароля.
Условия проверки:
длина пароля должна быть больше 6.
Входные данные: Строка.
Выходные данные: Логический тип."""

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")