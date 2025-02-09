a = eval(input("Enter a list of values: "))
i = 0

print("Before Remove List:", a)

while i < len(a):
    
    if a.count(a[i]) > 1:
        a.remove(a[i])
    else:
        i += 1
    
    
print("After Remove List:", a)
