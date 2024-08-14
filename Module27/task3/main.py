import functools
import logging
from datetime import datetime
from typing import Callable, Any

logging.basicConfig(filename='function_errors.log', level=logging.ERROR, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def logging_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для логирования информации о функции и записи ошибок в файл.

    :param func: Декорируемая функция.
    :return: Обёрнутая функция с логированием.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Вызов функции: {func.__name__}")
        print(f"Документация функции: {func.__doc__}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Ошибка в функции '{func.__name__}': {e}")
            print(f"Произошла ошибка: {e}")
            raise
    return wrapper

@logging_decorator
def example_function(a: int, b: int) -> int:
    """
    Пример функции, которая может вызвать ошибку деления на ноль.
    
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления.
    :raises ZeroDivisionError: Если второе число равно нулю.
    """
    return a / b

if __name__ == "__main__":
    try:
        example_function(10, 0)
    except ZeroDivisionError:
        print("Ошибка обработана.")
