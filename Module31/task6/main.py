import json
from typing import List, Dict, Any

def load_json(filename: str) -> Dict[str, Any]:
    """Загружает JSON-данные из файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def compare_json(old_data: Dict[str, Any], new_data: Dict[str, Any], keys_to_compare: List[str]) -> Dict[str, Any]:
    """Сравнивает значения по указанным ключам в двух словарях и возвращает различия."""
    differences = {}
    
    for key in keys_to_compare:
        if key in old_data and key in new_data:
            if old_data[key] != new_data[key]:
                differences[key] = new_data[key]
    
    return differences

def save_to_json(data: Dict[str, Any], filename: str) -> None:
    """Сохраняет данные в JSON-файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    """Основная функция для выполнения задачи."""
    diff_list = ['services', 'staff', 'datetime']
    
    try:
        old_data = load_json('json_old.json')
        new_data = load_json('json_new.json')
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON - {e}")
        return

    differences = compare_json(old_data['data'], new_data['data'], diff_list)
    
    print(differences)
    
    save_to_json(differences, 'result.json')

if __name__ == "__main__":
    main()
