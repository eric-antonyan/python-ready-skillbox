import re

plate_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car_pattern = r'\b[AВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'

taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b'

private_cars = re.findall(private_car_pattern, plate_numbers)
taxis = re.findall(taxi_pattern, plate_numbers)

print('Список номеров частных автомобилей:', private_cars)
print('Список номеров такси:', taxis)
