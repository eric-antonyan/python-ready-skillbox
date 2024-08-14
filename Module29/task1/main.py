from typing import Callable

user_permissions = ['admin']

def check_permission(required_permission: str) -> Callable:
    """
    Декоратор для проверки прав доступа пользователя.

    :param required_permission: Необходимое разрешение для доступа к функции.
    :return: Декорированная функция с проверкой прав доступа.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            if required_permission not in user_permissions:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_permission('admin')
def delete_site() -> None:
    """
    Функция для удаления сайта. Доступна только администраторам.
    """
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment() -> None:
    """
    Функция для добавления комментария. Доступна только пользователю с правами 'user_1'.
    """
    print('Добавляем комментарий')

try:
    delete_site()
except PermissionError as e:
    print(e)

try:
    add_comment()
except PermissionError as e:
    print(e)
