# Sum of Series of: x + x^2/2! + x^3/3! +.....+ x^n/n!
print("For the series: ")
print("x + x^2/2! + x^3/3! +.....+ x^n/n!\n")

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

f = 1
sum = 0

for i in range(1, n+1):
    if i == 1:
        print(x, end=' + ')
    elif i < n:
        print(f"{x}^{i}/{i}!", end=' + ')
    else:
        print(f"{x}^{i}/{i}!")
    
    f *= i
    sum += x ** i / f
    
print(f"The sum of series: {sum}")