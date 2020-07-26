"""
{1^2, 2^2 .....}
{x^2 | for all x in natural numbers}
{2x + 1 | for all x in integers}
{2n | n in (3, 10)}

[f(x) for x in iterable]
"""

# value = [x % 2 for x in range(1, 11)]
# print(value)

print(''.join([character.upper() for character in 'hello world']))
print(sum(n ** 2 for n in range(1, 4)))

val = min(x for x in range(1, 11))
print(val)
print(type(val))
