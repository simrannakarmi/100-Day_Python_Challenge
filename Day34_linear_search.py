ls = eval(input("Enter a List of numbers: "))
num = int(input("Enter number to be searched: "))

for i in range(len(ls)):
    if ls[i] == num:
         print("Found at Position", i + 1)
         break
else:
    print("Number not Found")