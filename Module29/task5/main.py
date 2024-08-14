from typing import Type, Callable, Any

def singleton(cls: Type) -> Type:
    """
    Декоратор для реализации паттерна Singleton.
    
    :param cls: Класс, который будет реализован как Singleton.
    :return: Класс, который гарантирует наличие только одного экземпляра.
    """
    instances = {}

    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Example:
    def __init__(self) -> None:
        pass

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
