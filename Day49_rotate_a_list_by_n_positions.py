A = eval(input("Enter the list of elements: "))
n = int(input("Enter the number of positions to shify: "))
print(A)

for i in range(n):
    temp = A[0]
    for j in range(len(A) - 1): 
        A[j] = A[j+1]   
    A[-1] = temp
    
print(A)