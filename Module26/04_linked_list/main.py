from typing import Any, Optional

class Node:
    """
    Класс для представления узла односвязного списка.
    """
    def __init__(self, data: Any, next: Optional['Node'] = None) -> None:
        self._data = data
        self._next = next

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @property
    def next(self) -> Optional['Node']:
        return self._next

    @next.setter
    def next(self, value: Optional['Node']) -> None:
        self._next = value


class LinkedList:
    """
    Класс для представления односвязного списка.
    """
    def __init__(self) -> None:
        self._head: Optional[Node] = None

    def append(self, data: Any) -> None:
        """
        Добавляет новый элемент в конец списка.
        :param data: Данные для добавления в список.
        """
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index: int) -> Any:
        """
        Получает элемент по индексу.
        :param index: Индекс элемента для получения.
        :return: Значение элемента по указанному индексу.
        :raises IndexError: Если индекс выходит за пределы списка.
        """
        current = self._head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1
        raise IndexError("Index out of bounds")

    def remove(self, index: int) -> None:
        """
        Удаляет элемент по индексу.
        :param index: Индекс элемента для удаления.
        :raises IndexError: Если индекс выходит за пределы списка.
        """
        if self._head is None:
            raise IndexError("Index out of bounds")

        if index == 0:
            self._head = self._head.next
            return

        current = self._head
        prev = None
        current_index = 0
        while current is not None:
            if current_index == index:
                prev.next = current.next
                return
            prev = current
            current = current.next
            current_index += 1
        raise IndexError("Index out of bounds")

    def __iter__(self):
        """
        Возвращает итератор для перебора элементов списка.
        """
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """
        Возвращает строковое представление списка.
        """
        return '[' + ' '.join(str(item) for item in self) + ']'


def main():
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print('Текущий список:', my_list)
    print('Получение третьего элемента:', my_list.get(2))
    print('Удаление второго элемента.')
    my_list.remove(1)
    print('Новый список:', my_list)

if __name__ == "__main__":
    main()
