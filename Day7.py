# Program to check if a year is leap year or not

year = int(input("Enter the year to be checked: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is a Leap Year.")
else:
    print(f"Year {year} is not a Leap Year.")

# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"Year {year} is a Leap Year.")
#     else:
#         print(f"Year {year} is not a Leap Year.")
# else:
#     if year % 4 == 0:
#         print(f"Year {year} is a Leap Year.")
#     else:
#         print(f"Year {year} is not a Leap Year.")
