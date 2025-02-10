numbers = eval(input("Enter the list of numbers: "))
n = len(numbers)

print("Before Selection Sort:", numbers)

for i in range(n-1):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            temp = numbers[i] 
            numbers[i] = numbers[j]
            numbers[j] = temp

print("After Selection Sort:", numbers)            