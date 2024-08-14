from typing import Callable, Dict, Optional

_routes: Dict[str, Callable[[], str]] = {}

def callback(route: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    """
    Декоратор для регистрации функции обратного вызова по указанному маршруту.

    :param route: Маршрут (путь), по которому будет доступна функция.
    :return: Декорированная функция, добавляющая функцию в словарь маршрутов.
    """
    def decorator(func: Callable[[], str]) -> Callable[[], str]:
        _routes[route] = func
        return func
    return decorator

class App:
    def __init__(self) -> None:
        self.routes = _routes

    def get(self, route: str) -> Optional[Callable[[], str]]:
        """
        Получение функции по маршруту.

        :param route: Маршрут (путь), по которому ищется функция.
        :return: Функция, зарегистрированная по этому маршруту, или None, если маршрут не найден.
        """
        return self.routes.get(route)

@callback('//')
def example() -> str:
    """
    Пример функции обратного вызова, которая возвращает ответ сервера.

    :return: Строка с ответом.
    """
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

app = App()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
