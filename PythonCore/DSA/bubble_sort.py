def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        sorted=False
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                sorted=True
        if not sorted:
            break
#unsorted integer list
lst=[64,25,12,22,11]
bubble_sort(lst)
print(lst)