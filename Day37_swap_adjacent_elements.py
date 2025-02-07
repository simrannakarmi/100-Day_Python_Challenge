a = eval(input("Enter the list of values: "))

print("Before Swap", a)

for i in range(0, len(a), 2):
    if i + 1 < len(a):
        a[i], a[i+1] = a[i+1], a[i]
            
print("After Swap: ", a) 
    
