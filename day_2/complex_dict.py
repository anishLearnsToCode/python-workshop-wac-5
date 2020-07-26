complex = {
    1: 12,
    'hello': 'word',
    'isOnline': True,
    3.14: 'pi',
    'pi': 3.14,
    range(1, 10, 2): [
        1,
        0.09,
        True,
        'name',
        range(5),
        [1, 2, 3],
        {
            'complex': [1, 2]
        }
    ],
    'frozen': {
        'odd': [1, 3, 5],
        'even': (2 * x for x in range(11)),
        'func': 'function',
        3: {
            'nested': True
        }
    }
}

print(complex['frozen'][3]['nested'])

print(complex.get('hello'))

print(type(complex))
del complex
print(complex)

iota = complex(0, 1)
print(iota)
print(type(iota))

print(type(sum))
sum = 10
print(type(sum))
print(sum([1, 2, 3]))
