def hcf(a, b):
    rem = a % b
    if rem == 0:
        return b
    res = hcf(b, rem)
    return res    
    
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

result = hcf(n1, n2)
print(f"The HCF of {n1} and {n2} is: {result}")