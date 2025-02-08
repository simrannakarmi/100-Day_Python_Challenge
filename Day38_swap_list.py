a = eval(input("Enter a list of values: "))
print("Before Swap", v)
n = len(a)

if n % 2 == 0:
    gap = n // 2
else:
    gap = n // 2 + 1
    
for  i in range(n // 2):
    temp = a[i]
    a[i] = a[i + 1]
    a[i+1] = temp 
    
   