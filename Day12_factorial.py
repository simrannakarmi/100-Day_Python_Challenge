# Factorial of a number

num = int(input("Enter a number: "))
fact = 1

for i in range(num, 0, -1):
    fact *= i

print(f"Factorial of {num} is {fact}")