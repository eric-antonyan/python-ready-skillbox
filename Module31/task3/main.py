import requests
import json

def get_xwing_info():
    starship_url = 'https://swapi.dev/api/starships/12/'

    response = requests.get(starship_url)
    response.raise_for_status()  # Проверяем на ошибки
    starship_data = response.json()

    xwing_info = {
        'название': starship_data['name'],
        'максимальная скорость': starship_data['max_atmosphering_speed'],
        'класс': starship_data['starship_class'],
        'список пилотов': []
    }

    pilot_urls = starship_data['pilots']
    for pilot_url in pilot_urls:
        pilot_response = requests.get(pilot_url)
        pilot_response.raise_for_status()
        pilot_data = pilot_response.json()
        
        pilot_info = {
            'имя': pilot_data['name'],
            'рост': pilot_data['height'],
            'вес': pilot_data['mass'],
            'родная планета': pilot_data['homeworld'],
            'ссылка на информацию о родной планете': pilot_data['homeworld']
        }
        
        xwing_info['список пилотов'].append(pilot_info)

    return xwing_info

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    xwing_info = get_xwing_info()
    
    print('Информация о X-wing:')
    print(json.dumps(xwing_info, ensure_ascii=False, indent=4))
    
    save_to_json(xwing_info, 'xwing_info.json')

if __name__ == "__main__":
    main()
