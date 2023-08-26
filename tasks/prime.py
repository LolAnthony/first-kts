__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 0 or number == 1:
        return False
    d = 2
    while d <= number**(1/2):
        if number % d == 0:
            return False
        d += 1
    return True
