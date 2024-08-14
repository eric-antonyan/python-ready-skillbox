import functools

def how_are_you(func: callable) -> callable:
    """
    Декоратор, который спрашивает у пользователя 'Как дела?' перед вызовом декорируемой функции.
    После того, как пользователь ответит, декоратор выводит 'А у меня не очень!' и затем вызывает функцию.

    :param func: Декорируемая функция.
    :return: Обёрнутая функция.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        user_response = input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)

    return wrapper

@how_are_you
def test() -> None:
    """
    Пример функции, которая будет декорирована и вызвана.
    """
    print("<Тут что-то происходит...>")

# Вызов декорированной функции
if __name__ == "__main__":
    test()
