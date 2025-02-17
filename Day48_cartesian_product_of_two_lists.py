A = eval(input("Enter the elements of first list: "))
B = eval(input("Enter the elements of second list: "))

R = []

for i in A:
    for j in B:
        R.append((i, j))
        
print("List 1:", A)
print("List 2:", B)
print("Cartesian Product:", R)