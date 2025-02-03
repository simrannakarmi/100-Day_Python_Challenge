import random

num = random.randint(10, 60)

for i in range(5):
    guess = int(input("Enter a number between 10 to 60: "))
    
    if num == guess:
        print("*" * 20)
        print("     YOU WIN")
        print("*" * 20)
        break
    elif num > guess:
        print("\nSorry, the number is greater than your guess.\n")
    elif num < guess:
        print("\nSorry, the number is lesser than your guess.\n")
else:
    print("-" * 20)
    print("     YOU LOOSE")
    print("-" * 20)