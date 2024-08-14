import os
from typing import Generator

def count_non_empty_code_lines(file_path: str) -> int:
    """
    Считает количество непустых строк и строк кода (игнорирует пустые строки и комментарии)
    в указанном Python-файле.

    :param file_path: Путь к Python-файлу.
    :return: Количество непустых строк и строк кода в файле.
    """
    code_lines = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    code_lines += 1
    except Exception as e:
        print(f"Не удалось прочитать файл {file_path}: {e}")
    return code_lines

def gen_file_line_counts(root_dir: str) -> Generator[int, None, None]:
    """
    Генерирует количество непустых строк кода для каждого Python-файла в указанной директории и её подпапках.

    :param root_dir: Корневая директория для поиска Python-файлов.
    :return: Генератор количества строк в каждом Python-файле.
    """
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                yield count_non_empty_code_lines(file_path)

def main():
    try:
        root_dir = input("Введите путь к корневой директории (по умолчанию текущая директория): ") or "."

        print(f"Количество строк кода в Python-файлах в директории '{root_dir}':")
        for line_count in gen_file_line_counts(root_dir):
            print(line_count)
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
