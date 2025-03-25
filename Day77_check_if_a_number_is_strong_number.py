# Strong Number -> Factorial of Digits are added to get the same number
# 145 -> 1! + 2! + 3! = 1 + 24 + 120 = 145

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1) 


num = int(input("Enter a number: "))

sum = 0
n = num

while num != 0:
    rem = num % 10
    sum += factorial(rem)
    num = num // 10
    
print("Sum is:", sum)
if sum == n:
    print(n, "is a Strong Number.")
else:
    print(n, "is Not a Strong Number.")
    