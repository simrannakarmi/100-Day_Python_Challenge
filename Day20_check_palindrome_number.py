n = num = int(input("Enter a number to be checked: "))
rev = 0

while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
    
print(f"The reverse of {num} is: {rev}.")

if num == rev:
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is not a Palindrome Number.")
    