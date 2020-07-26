"""
Map operator
map(function, iterable)

for index in range(len(iterable)):
    iterable[index] = function(iterable[index])

    x1 x2 x3 x4 ... xn
    f(x1) f(x2) f(x3) .... f(xn)
"""


def increment(number):
    return number + 10


value = list(map(increment, [1, 2, 3, 4]))
print(type(value))
print(value)

# numbers = list(map(int, input().split()))

# print(type(numbers))
# print(type(numbers[0]))
# print(numbers)
