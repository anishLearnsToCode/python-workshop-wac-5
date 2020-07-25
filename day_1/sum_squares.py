n = int(input())

# 1^2 + 2^2 + 3^2 + ... + n^2
sum = 0
i = 1
while i <= n:
    sum += i * i
    i += 1
print(sum)
