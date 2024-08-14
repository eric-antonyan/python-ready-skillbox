import os
from typing import Generator

def error_log_generator(log_file_path: str) -> Generator[str, None, None]:
    """
    Генератор, который считывает строки из файла и возвращает только те строки,
    которые содержат слово 'ERROR'.

    :param log_file_path: Путь к файлу с логами.
    :yield: Строки, содержащие слово 'ERROR'.
    """
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if 'ERROR' in line:
                    yield line
    except FileNotFoundError:
        print(f"Файл {log_file_path} не найден.")
    except IOError as e:
        print(f"Ошибка при чтении файла {log_file_path}: {e}")

def write_errors_to_file(input_file_path: str, output_file_path: str) -> None:
    """
    Записывает строки, содержащие 'ERROR', из входного файла в выходной файл.

    :param input_file_path: Путь к входному файлу с логами.
    :param output_file_path: Путь к выходному файлу, куда будут записаны строки с 'ERROR'.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for error_line in error_log_generator(input_file_path):
                output_file.write(error_line)
    except IOError as e:
        print(f"Ошибка при записи в файл {output_file_path}: {e}")

def main():
    input_file_path = input("Введите путь к входному файлу с логами: ")
    output_file_path = input("Введите путь к выходному файлу для записи ошибок: ")

    write_errors_to_file(input_file_path, output_file_path)
    print(f"Ошибки были записаны в файл {output_file_path}")

if __name__ == "__main__":
    main()
