"""
Cas classique
"""

def sum_numbers(from_number: int, to_number: int):
    numbers = range(from_number, to_number + 1)
    return sum(numbers)

a : int = 1
b : int = 5
print(f"Somme des nombre de {a} à {b} : = {sum_numbers(a, b)}")

print(type(b)) # type 'int'

SomeData = 15
print(type(SomeData)) # type 'int'

SomeData = True
print(type(SomeData)) # type 'bool'

SomeData = (15, )
print(type(SomeData)) # type 'tuple'
