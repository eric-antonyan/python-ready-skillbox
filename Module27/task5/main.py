import functools
from typing import Callable, Any

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для кэширования результатов вызова функции.
    Кэширование происходит с помощью словаря, где ключами являются аргументы функции,
    а значениями - результаты её выполнения.

    :param func: Декорируемая функция.
    :return: Обёрнутая функция с кэшированием результатов.
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if (args, frozenset(kwargs.items())) in cache:
            return cache[(args, frozenset(kwargs.items()))]
        result = func(*args, **kwargs)
        cache[(args, frozenset(kwargs.items()))] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи рекурсивно.

    :param n: Индекс числа Фибоначчи.
    :return: Значение n-го числа Фибоначчи.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
