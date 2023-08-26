__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    """
    minutes = int(seconds / 60 % 60)
    hours = int(seconds / 60 / 60 % 24)
    days = int(seconds / 60 / 60 / 24)

    seconds %= 60

    seconds_str = f'{seconds % 60}s' if seconds > 9 else f'0{seconds % 60}s'
    minutes_str = f'{minutes}m' if minutes > 9 else f'0{minutes}m'
    hours_str = f'{hours}h' if hours > 9 else f'0{hours}h'
    days_str = f'{days}d' if days > 9 else f'0{days}d'

    if days:
        time_str = days_str + hours_str + minutes_str + seconds_str
    elif hours:
        time_str = hours_str + minutes_str + seconds_str
    elif minutes:
        time_str = minutes_str + seconds_str
    else:
        time_str = seconds_str

    return time_str
