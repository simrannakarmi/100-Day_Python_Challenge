def partition(a, left, right):
    i = left - 1
    pivot = right
    
    for j in range(left, right):
        if a[j] < a[pivot]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[pivot] = a[pivot], a[i+1]
    return i+1

def quicksort(a, left, right):
    if right - left > 1:
        p = partition(a, left, right)
        quicksort(a, left, p-1)
        quicksort(a,  p+1, right)
    else:
        return
    
n = eval(input("Enter a list of numbers: "))
print("BEFORE SORTING")
print(n)
quicksort(n, 0, len(n)-1)
print("AFTER SORTING")
print(n)