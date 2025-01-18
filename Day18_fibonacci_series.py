n = int(input("Enter the number of elements: "))

a = 0
b = 1

if n >= 2:
    print("The fibonacci series:")
    print(a, b, end=' ')
    for i in range(n-2):
        c = a + b
        print(c, end=' ')
        a = b
        b = c
else:
    print("Please enter two or more number of elements for fibonacci series.")
