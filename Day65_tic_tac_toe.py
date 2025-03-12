import random

grid = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

def show():
    print()
    print("-" * 13)
    print("| "+grid[1]+" | "+grid[2]+" | "+grid[3]+" |")
    print("-" * 13)
    print("| "+grid[4]+" | "+grid[5]+" | "+grid[6]+" |")
    print("-" * 13)
    print("| "+grid[7]+" | "+grid[8]+" | "+grid[9]+" |")    
    print()
    
print("-" * 24)
print(" Welcome to Tic Tac Toe")
print("-" * 24)
print("1. Single Player (Human VS Robot)")
print("2. Two Player (Human VS Human)")
choice = int(input("\nEnter your choice: "))

if choice == 1:
    p1 = input("\nEnter Player's name: ")
    p2 = "Bot"   
elif choice == 2:
    p1 = input("\nEnter Player 1's name: ")
    p2 = input("Enter Player 2's name: ")
else:
    print("Invalid choice")
    exit()

print(f"\n{p1} VS {p2}")

turn = 1

while True:
    show()
    if turn % 2 == 1:
        pos = int(input(p1+": Enter the position to place X (1-9): "))
        if pos in grid and grid[pos] == " ":
            grid[pos] = "X"
            turn += 1
    else:
        if p2 == "Bot":
            pos = random.randint(1,9)
            print(f"{p2}: {pos}")
        else:
            pos = int(input(p2+": Enter the position to place O (1-9): "))
            
        if pos in grid and grid[pos] == " ":
            grid[pos] = "O"
            turn += 1
        
    if grid[1] == grid[2] == grid[3] and grid[1]!=" ":
        show()
        if grid[1] == 'X':
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[4] == grid[5] == grid[6] and grid[4]!=" ":
        show()
        if grid[4] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[7] == grid[8] == grid[9] and grid[7]!=" ":
        show()
        if grid[7] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[1] == grid[4] == grid[7] and grid[1]!=" ":
        show()
        if grid[1] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[2] == grid[5] == grid[8] and grid[2]!=" ":
        show()
        if grid[4] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[3] == grid[6] == grid[9] and grid[3]!=" ":
        show()
        if grid[3] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[1] == grid[5] == grid[9] and grid[1]!=" ":
        show()
        if grid[1] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif grid[3] == grid[5] == grid[7] and grid[3]!=" ":
        show()
        if grid[3] == "X":
            print(p1, " Wins")
        else:
            print(p2, " Wins")
        break
    elif turn > 9:
        show()
        print("Its a DRAW")
        break
    