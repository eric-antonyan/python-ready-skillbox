import functools
import datetime
from typing import Type, Callable

def log_methods(date_format: str) -> Callable[[Type], Type]:
    """
    Декоратор для логирования вызовов методов класса.

    :param date_format: Формат вывода даты и времени.
    :return: Декорированный класс с логированием методов.
    """
    def decorator(cls: Type) -> Type:
        def get_formatted_time() -> str:
            return datetime.datetime.now().strftime(date_format)

        def log_method_call(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(self, *args, **kwargs):
                start_time = datetime.datetime.now()
                formatted_time = get_formatted_time()
                print(f"Запускается '{self.__class__.__name__}.{func.__name__}'. Дата и время запуска: {formatted_time}.")
                result = None
                try:
                    result = func(self, *args, **kwargs)
                finally:
                    end_time = datetime.datetime.now()
                    duration = (end_time - start_time).total_seconds()
                    print(f"Завершение '{self.__class__.__name__}.{func.__name__}', время работы = {duration:.3f} s.")
                return result
            return wrapper

        for attr_name in dir(cls):
            if not attr_name.startswith('__'):
                attr = getattr(cls, attr_name)
                if callable(attr):
                    setattr(cls, attr_name, log_method_call(attr))

        return cls
    
    return decorator

@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
