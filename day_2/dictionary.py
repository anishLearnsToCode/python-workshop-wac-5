"""
Dictionary / Map / HashMap

index --> value
int   --> anything
unique --> not unique

query: string
list: [list[websites]]

key --> value
(anything) --> (anything)
unique          not unique

{}
(key, value)
"""

words = {
    'i': 34,
    'am': 34,
    'batman': 10
}

print(type(words))

print(words)
words['ball'] = 3
print(words)

words['batman'] = 0
print(words)

if 'batman' in words:
    del words['batman']

print(words, end='\n\n\n')

# keys = words.keys()
# print(type(keys))
# print(keys)

# values = words.values()
# print(type(values))
# print(values)

# items = words.items()
# print(type(items))
# print(items)

for key, value in words.items():
    print('key: ' + key + ' value: ' + str(value))
