# Print:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

num = int(input("Enter the number of rows: "))

for i in range(1, num+1):
    for j in range(num-i):
        print(" ", end='')
    for k in range(2*i -1 ):
        print("*", end='')
    print()

for i in range(num-1, 0, -1):
    for j in range(num-i):
        print(" ", end='')
    for k in range(2*i -1 ):
        print("*", end='')
    print()