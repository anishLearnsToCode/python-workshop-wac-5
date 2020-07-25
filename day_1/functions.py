"""
Functions
def functionName(parameter1, parameter2, parameter3 ....):
    code
    return value1, value2, .. (not compulsory)
"""

# print('text', end='  *** ')
# value = type('hello')
# print(value)


def helloWorld():
    print('hello world')
    print('i have been invoked')


def hello():
    print('i am in hello()')


def embed():
    def embedded():
        print('this is embedded function')
    return embedded


def sandwichCreator(dimensions):
    def createSandwich(sauce):
        print('creating sandwich with ' + sauce + ' and ' + str(dimensions))
    return createSandwich


# helloWorld()
# hello()
# helloWorld()
# helloWorld()
# helloWorld()
# hello()
# helloWorld()

# value = embed()
# print(type(value))
# value()

sixFootCreator = sandwichCreator(6)
twelveFootCreator = sandwichCreator(12)
jumboSandwichCreator = sandwichCreator(20)
# print(type(sixFootCreator))
# print(type(twelveFootCreator))
# print(type(jumboSandwichCreator))

jumboSandwichCreator('mustard')
jumboSandwichCreator('honey')
sixFootCreator('ketchup')
