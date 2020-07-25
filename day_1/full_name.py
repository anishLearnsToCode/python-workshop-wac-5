def fullName(firstName, lastName=''):
    print(firstName + ' ' + lastName)


def fullNameMiddleName(firstName, lastName, middleName=''):
    if middleName:
        return firstName + ' ' + middleName + ' ' + lastName
    else:
        return firstName + ' ' + lastName


def sumNNumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# fullName('anish', 'sachdeva')
# fullName('john', 'doe')
# fullName('martha')
# fullName(lastName='wick', firstName='john')
# fullName(firstName='john')
# print('text', end='**')

# name = fullNameMiddleName('woplfgang', 'mozart')
# print(name)
