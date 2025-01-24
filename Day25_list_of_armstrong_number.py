
print("To check the Armstrong Number:")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


for num in range(start, end + 1):
    n = num
    sum = 0
    no_of_digit = len(str(num))

    while n != 0:
        rem = n % 10
        sum += rem ** no_of_digit
        n = n // 10
    
    if num == sum:
        print(f"{num} is Armstrong Number")