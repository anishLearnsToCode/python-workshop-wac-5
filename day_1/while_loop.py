"""
While Loop
while predicate:
    code

predicate --> code --> predicate --> code --> predicate --> code --> predicate false --> exit loop
"""

# infinite loop
# while True:
#     print('hello world')

iterations = int(input())
i = 0
while i < iterations:
    print('hello world : ' + str(i))
    i += 1

print('out of loop')
