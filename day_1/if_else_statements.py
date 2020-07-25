"""
If else

if predicate:
    code
    code
elif predicate2: (not compulsory)
    code
elif predicate3:
    code
elif predicate4:
    code
..
..
..
else:       (not compulsory)
    code
"""
number = int(input())

if number == 1:
    print('i am in if block')
    print('i am having fun')
elif number == 2:
    print('wow')
elif number == 3:
    print('mehhhhhhh')
elif number == 100:
    print('large number')
    print('super large number')

print('i am outside if else block')
