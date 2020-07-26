numbers = list(map(int, input().split()))
sumNumbers = sum(numbers)
largest = max(numbers)
smallest = min(numbers)
smallestSum = sumNumbers - largest
largestSum = sumNumbers - smallest
print(smallestSum, end=' ')
print(largestSum)
