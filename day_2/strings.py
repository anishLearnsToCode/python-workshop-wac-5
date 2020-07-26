"""
Strings
- strings are immutable
"""


def findSecond(string, search):
    index = string.find(search)
    return index + 1 + string[index + 1:].find(search)


# val = 'hello'
# print(id(val))
# print(id('hello'))
# val = val.upper()
# print(id(val))
# print(id('HELLO'))
# print(id('HELLO'))
# print(id('HELLO'))
print(findSecond('lolipop', 'p'))
# val = 'hello'
# print(id(val))
