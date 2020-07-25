from day_1.full_name import sumNNumbers


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def permutation(n, r):  # nPr = n! / (n - r)!
    return factorial(n) // factorial(n - r)


def combination(n, r):  # nCr = n! / ((n - r)! * r!) = nPr / r!
    return permutation(n, r) // factorial(r)

print(combination(5, 0))
print(combination(5, 1))
print(combination(5, 2))
print(combination(5, 3))
print(combination(5, 4))
print(combination(5, 5))
