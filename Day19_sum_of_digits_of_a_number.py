n = num = int(input("Enter a number: "))

sum = 0

while n != 0:
    rem = n % 10
    sum += rem
    n = n // 10
    
print(f"The sum of digits of {num} is: {sum}")