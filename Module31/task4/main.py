import re

def validate_phone_numbers(phone_numbers):
    pattern = r'^([89]\d{9})$'
    
    for index, number in enumerate(phone_numbers):
        if re.match(pattern, number):
            print(f'{index + 1}-й номер: всё в порядке')
        else:
            print(f'{index + 1}-й номер: не подходит')

def main():
    phone_numbers = ['9999999999', '999999-999', '99999x9999']
    
    validate_phone_numbers(phone_numbers)

if __name__ == "__main__":
    main()
