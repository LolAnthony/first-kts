from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.

    """

    new_dict = dict(zip(d.values(), d.keys()))
    return new_dict


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.

    """

    new_d = {}
    for i in d.values():
        new_d[i] = []
    for i in d.keys():
        new_d[d[i]].append(i)
    return new_d
