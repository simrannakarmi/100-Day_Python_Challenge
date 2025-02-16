l1 = eval(input("Enter first list: "))
l2 = eval(input("Enter second list: "))

union = l1.copy()
intersection = []

for i in l2:
    if i in l1:
        intersection.append(i)
    else:
        union.append(i)

print("List 1:", l1)
print("List 2:", l2)
print("The union is:", union)        
print("The intersection is:", intersection)        
    