# Left shift

def LShift(arr, n):
    for i in range(n):
        val = arr.pop(0)
        arr.append(val)
    
    print(arr)
    
a = [10,20,30,40,17,19,22]
LShift(a, 2)