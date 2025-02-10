numbers = eval(input("Enter the list of numbers: "))

highest = second = 0

for num in numbers:
    if num > highest:
        second = highest
        highest = num
    elif num > second and num != highest:
        second = num
        
if second == 0:
    print("No second highest number.")
else:
    print("Second highest number:", second)
        