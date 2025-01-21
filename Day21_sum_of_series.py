n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    if i < n:
        print("1/" + str(i), end=' + ')
    else:
        print("1/" + str(i))
    sum += 1/i
    
print(f"Sum is: {round(sum, 2)}")
        