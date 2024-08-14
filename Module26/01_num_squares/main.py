from typing import Iterator, Generator

class SquareIterator(Iterator):
    """
    Итератор для генерации квадратов чисел от 1 до N.
    """
    def __init__(self, n: int):
        self._n = n
        self._current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self._current > self._n:
            raise StopIteration
        square = self._current ** 2
        self._current += 1
        return square

def generate_squares(n: int) -> Generator[int, None, None]:
    """
    """
    for i in range(1, n + 1):
        yield i ** 2

def main():
    try:
        n = int(input("Введите число N: "))

        print("Использование класса-итератора:")
        squares = SquareIterator(n)
        for square in squares:
            print(square)
        
        print("\nИспользование функции-генератора:")
        for square in generate_squares(n):
            print(square)
        
        print("\nИспользование генераторного выражения:")
        squares_gen_expr = (i ** 2 for i in range(1, n + 1))
        for square in squares_gen_expr:
            print(square)

    except ValueError:
        print("Введите корректное число.")

if __name__ == "__main__":
    main()
