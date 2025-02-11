numbers = eval(input("Enter the list of numbers: "))
n = len(numbers)

print("Before Bubble Sort:", numbers)

for i in range(n-1):
    for j in range(0, n-1-i):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
        
print("After Bubble Sort:", numbers)