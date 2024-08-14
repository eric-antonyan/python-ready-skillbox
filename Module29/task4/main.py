from typing import Callable, Any

def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор для декораторов, который позволяет декораторам принимать произвольные аргументы.
    
    :param decorator: Декоратор, который должен быть обёрнут.
    :return: Функция-декоратор, которая принимает произвольные аргументы и ключевые слова.
    """
    def wrapper(*args, **kwargs) -> Callable:
        def actual_decorator(func: Callable) -> Callable:
            decorated_func = decorator(*args, **kwargs)(func)
            return decorated_func
        return actual_decorator
    return wrapper

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args: Any, **kwargs: Any) -> Callable:
    """
    Пример декоратора, который принимает произвольные аргументы и ключевые слова.
    
    :param func: Функция, которую нужно декорировать.
    :param args: Аргументы, переданные в декоратор.
    :param kwargs: Ключевые слова, переданные в декоратор.
    :return: Декорированная функция.
    """
    def wrapper(*func_args: Any, **func_kwargs: Any) -> Any:
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """
    Пример декорируемой функции, которая принимает текст и число.
    
    :param text: Текстовая строка.
    :param num: Число.
    """
    print("Привет", text, num)

decorated_function("Юзер", 101)
