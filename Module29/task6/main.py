import time
import functools
from typing import Callable, Any

class LoggerDecorator:
    """
    Класс-декоратор для логирования аргументов, результатов и времени выполнения функции.
    """
    
    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            
            print(f"Вызов функции {func.__name__}")
            print(f"Аргументы: {args}, {kwargs}")
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            print(f"Результат: {result}")
            print(f"Время выполнения: {execution_time} секунд")
            
            return result
        
        return wrapper

@LoggerDecorator()
def complex_algorithm(arg1: int, arg2: int) -> int:
    """
    Пример сложного алгоритма для демонстрации работы декоратора.

    :param arg1: Первое значение для алгоритма.
    :param arg2: Второе значение для алгоритма.
    :return: Результат вычислений.
    """
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result

result = complex_algorithm(10, 50)
