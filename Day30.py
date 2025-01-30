# Print:
# **************
# ******  ******
# *****    *****
# ****      ****
# ***        ***
# **          **
# *            *
# *            *
# **          **
# ***        ***
# ****      ****
# *****    *****
# ******  ******
# **************

n = int(input("How many rows are there: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    for k in range(2*(n-i)):
        print(" ", end='')
    for l in range(i):
        print("*", end='')
    print()
    
for i in range(1, n+1):
    for j in range(i):
        print("*", end='')
    for k in range(2*(n-i)):
        print(" ", end='')
    for l in range(i):
        print("*", end='')
    print()