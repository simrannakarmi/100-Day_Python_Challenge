a = eval(input("Enter a list of numbers: "))
n = len(a)

for i in range(n // 2):
    a[i], a[n-i-1] = a[n-i-1], a[i]
    
print("\nThe reversed list:", a)