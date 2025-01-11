# Program to Grade a Student as per percentage marks

percentage = float(input("Enter the percentage marks secured: "))

if percentage >= 90:
    print("Grade is A+")
elif percentage >= 80:
    print("Grade is A")
elif percentage >= 70:
    print("Grade is B+")
elif percentage >= 60:
    print("Grade is B")
elif percentage >= 50:
    print("Grade is C")
elif percentage >= 40:
    print("Grade is D")
else:
    print("Grade is F")
    
