n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 > n2:
    g = n1
else:
    g = n2
    
for i in range(g, n1*n2 + 1):
    if i % n1 == 0 and i % n2 == 0:
        print(f"LCM of {n1} and {n2} is {i}")
        break
    