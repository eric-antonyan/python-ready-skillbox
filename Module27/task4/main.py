import functools
from typing import Callable, Any

def counter(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор, который считает и выводит количество вызовов декорируемой функции.

    :param func: Декорируемая функция.
    :return: Обёрнутая функция с подсчётом вызовов.
    """
    # Словарь для хранения счётчика вызовов функции
    call_count = {'count': 0}
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        call_count['count'] += 1
        print(f"Функция '{func.__name__}' вызвана {call_count['count']} раз(а).")
        return func(*args, **kwargs)
    
    return wrapper

@counter
def example_function(a: int, b: int) -> int:
    """
    Пример функции для демонстрации работы декоратора счётчика.

    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма двух чисел.
    """
    return a + b

if __name__ == "__main__":
    print(example_function(1, 2))
    print(example_function(3, 4))
    print(example_function(5, 6))
