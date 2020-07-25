n = int(input())

# n! = 1 * 2 * 3 * ... * n
# 0! = 1

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)
