__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    """
    even = sum(filter(lambda x: x % 2 == 0, arr))
    odd = sum(filter(lambda x: x % 2, arr))
    return even/odd if odd != 0 else 0
