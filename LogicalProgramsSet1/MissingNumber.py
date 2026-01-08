n = int(input())
numbers = list(map(int, input().split()))
total = n * (n + 1) // 2
given_sum = sum(numbers)
missing = total - given_sum
print("Missing number is:", missing)
 