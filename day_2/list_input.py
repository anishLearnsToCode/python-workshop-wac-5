# 1 3 4 -100 90 3
numbers = input().split()
print(type(numbers))
print(numbers)
print(type(numbers[0]))

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

print(type(numbers))
print(numbers)
print(type(numbers[0]))
