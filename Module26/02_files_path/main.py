import os
from typing import Generator

def gen_files_path(root_dir: str, target_dir: str) -> Generator[str, None, None]:
    """
    Рекурсивно проходит по всем каталогам и генерирует пути всех встреченных файлов
    в указанной директории и её подпапках.

    :param root_dir: Корневая директория для начала поиска. По умолчанию - текущая директория.
    :param target_dir: Искомая директория. Все файлы из этой директории и её подпапок будут сгенерированы.
    :return: Генератор путей файлов.
    """
    for root, dirs, files in os.walk(root_dir):
        if target_dir in os.path.relpath(root, root_dir):
            for file in files:
                yield os.path.join(root, file)

def main():
    try:
        root_dir = input("Введите путь к корневой директории (по умолчанию текущая директория): ") or "."
        target_dir = input("Введите имя целевой директории: ")

        print(f"Поиск файлов в директории '{target_dir}' и её подпапках:")
        for file_path in gen_files_path(root_dir, target_dir):
            print(file_path)
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
