from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words_sorted = list(sorted(text.split(), key=lambda x: len(x)))
    if words_sorted and words_sorted[0] != words_sorted[-1]:
        return words_sorted[0], words_sorted[-1]
    return None, None
