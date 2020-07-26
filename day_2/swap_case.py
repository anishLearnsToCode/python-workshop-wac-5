def swapCase(string):
    # acc = ''
    # for character in string:
    #     if character.islower():
    #         acc += character.upper()
    #     else:
    #         acc += character.lower()
    # return acc

    return ''.join([character.lower() if character.isupper() else character.upper() for character in string])


print(swapCase('anish'))
print(swapCase('hello world'))
print(swapCase('HELLO'))
print(swapCase('Hello WoRLd'))
