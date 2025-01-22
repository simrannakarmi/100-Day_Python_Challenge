# Sum of series: x^1 + x^2 + x^3 +.....+ x^n

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

sum = 0

for i in range(1, n+1):
    if i < n:
        print(f"{x}^{i}", end=' + ')
    else:
        print(f"{x}^{i}")
        
    sum += x ** i
    
print(f"Sum: {sum}")
