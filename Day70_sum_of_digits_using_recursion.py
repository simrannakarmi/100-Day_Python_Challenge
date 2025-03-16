def sum_of_digits(n):
    if n == 0:
        return 0
    
    rem = n % 10
    n = n // 10
    res = rem + sum_of_digits(n)
    return res

num = int(input("Enter a number: "))

result = sum_of_digits(num)

print("Sum of Digits of ", num,"is: ", result)