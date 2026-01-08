lst = list(map(int, input().split()))
duplicates = list({x for x in lst if lst.count(x) > 1})
print(duplicates)
