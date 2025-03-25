# Automorphic Number -> if the square ends with the same digit as the number itself.
# 5^2 -> 25 

num = int(input("Enter a number: "))
sq = num ** 2

print("Square is:", sq)
n = len(str(num))
end = sq % 10 ** n

if num == end:
    print(num, "is an Automorphic Number.")
else:
    print(num, "is NOT an Automorphic Number.")
