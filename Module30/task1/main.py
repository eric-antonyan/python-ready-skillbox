from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

cubed_rounded_floats = list(map(lambda x: round(x ** 3, 3), floats))

long_names = list(filter(lambda name: len(name) >= 5, names))

product_of_numbers = reduce(lambda x, y: x * y, numbers)

print("Cubed and rounded floats:", cubed_rounded_floats)
print("Long names:", long_names)
print("Product of numbers:", product_of_numbers)
