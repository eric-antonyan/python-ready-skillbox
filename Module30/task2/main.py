letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]

results = list(map(lambda i: (letters[i], numbers[i]), range(len(letters))))

print(results)
