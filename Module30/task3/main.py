from collections import Counter

def can_be_poly(s: str) -> bool:
    """
    Проверяет, можно ли из строки составить палиндром.

    :param s: Строка для проверки.
    :return: True, если из строки можно составить палиндром, иначе False.
    """
    counter = Counter(s)
    
    odd_count = sum(1 for count in counter.values() if count % 2 != 0)
    
    return odd_count <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
