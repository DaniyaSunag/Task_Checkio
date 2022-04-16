"""Любой настоящий путешественник должен уметь делать три вещи: добывать огонь, находить воду и извлекать полезную информацию из природы, окружающей его.
Программирование не поможет вам с огнем и водой, но с добычей информации справится вполне.
Ваша задача - определить угол солнца над горизонтом, зная время суток. Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".
Входные данные: Время.
Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой."""


from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    if 600 <= int(time.replace(':', '')) <= 1800:
        h, m = map(int, time.split(':'))
        minute = (h - 6) * 60 + m
        return angle_in_minute * minute
    return 'I don\'t see the sun!'


angle_in_minute = 180 / (12 * 60)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")