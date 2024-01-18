
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get even numbers: 
even= list(filter(lambda x: x % 2 == 0, numbers))

# Using map to square each number:
square= list(map(lambda x: x ** 2, numbers))

# Using reduce to find total:
from functools import reduce
total = reduce(lambda x, y: x +y, numbers)

print("Even numbers:", even)
print("Squared numbers:", square)
print("Product of numbers:", total)
