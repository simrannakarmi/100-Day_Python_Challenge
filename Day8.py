# Program to check if a triangle is equilateral or isosceles or scalene triangle

a = int(input("Enter first side of a triangle: "))
b = int(input("Enter second side of a triangle: "))
c = int(input("Enter third side of a triangle: "))

if a == b and b == c:
    print("The Triangle is Equilateral.")
elif a == b or b == c or c == a:
    print("The Traingle is Isosceles.")
else:
    print("The Traingle is Scalene.")
