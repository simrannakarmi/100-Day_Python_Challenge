# Program to check perfect number. (If a sum of factors is equal to the number itself.)

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i
        
if num == sum:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
     