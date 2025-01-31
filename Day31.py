# Print:
# *           *           * * * * * * *
#   *       *             * *       * *
#     *   *               *   *   *   *
#       *         or      *     *     *
#     *   *               *   *   *   *
#   *       *             * *       * *
# *           *           * * * * * * *

n = int(input("Enter the number of lines or rows: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or i + j == n + 1 or i == 1 or i == n or j == 1 or j == n:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

