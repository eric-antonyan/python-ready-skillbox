import time
import functools
from typing import Callable, Any

def delay(seconds: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор, который задерживает выполнение декорируемой функции на указанное количество секунд.

    :param seconds: Количество секунд, на которое нужно задержать выполнение.
    :return: Обёрнутая функция с задержкой.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Ожидание {seconds} секунд(ы) перед выполнением функции...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(3)
def example_function() -> None:
    """
    Пример функции, выполнение которой будет замедлено.
    """
    print("Функция выполнена!")

if __name__ == "__main__":
    example_function()
