a = eval(input("Enter the list: "))
num = int(input("Enter the number to be searched: "))

beg = 0
end = len(a) - 1

while beg <= end:
    mid = (beg + end) // 2
    if a[mid] == num:
        print("\nFound at Position:", mid+1)
        break
    elif num > a[mid]:
        beg = mid+1
    elif num < a[mid]:
        end = mid -1
else:
    print("\nNumber not Found")