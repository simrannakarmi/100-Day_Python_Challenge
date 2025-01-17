def hcf(n1, n2):
    rem = 0
    while n1 % n2 != 0:
        rem = n1 % n2
        n1 = n2
        n2 = rem
        
    return rem

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = hcf(a, b)
    
print(f"HCF of {a} and {b} is {result}")