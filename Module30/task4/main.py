from collections import Counter

def count_unique_characters(message: str) -> int:
    """
    Определяет количество уникальных символов в строке, игнорируя регистр и неалфавитные символы.

    :param message: Строка, в которой нужно найти уникальные символы.
    :return: Количество уникальных символов.
    """
    filtered_message = filter(lambda char: char.isalpha(), message.lower())
    
    count = Counter(filtered_message)
    
    unique_count = sum(1 for _, occurrence in count.items() if occurrence == 1)
    
    return unique_count

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
