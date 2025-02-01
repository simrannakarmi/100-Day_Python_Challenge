import random
import time

name1 = input("Enter the name of Player 1: ")
name2 = input("Enter the name of Player 2: ")

val1 = random.randint(1, 6)
val2 = random.randint(1, 6)

time.sleep(2)

print("Player 1 got", val1)
print("Player 2 got", val2)

time.sleep(2)

if val1 > val2:
    print(f"Player 1: {name1} Wins")
elif val1 < val2:
    print(f"Player 2: {name2} Wins")
else:
    print("It is a DRAW")