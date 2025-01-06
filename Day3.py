# input name, marks of five subjects of a student,
# print total, percentage, pass or fail
# if pass: congratulation! You are promoted to another class.
# if fail: Sorry, you have to appear next year

name = input("Enter your name: ")
no_of_subjects = int(input("Enter no. of subjects: "))
total_marks = 0
marks_info = {}

for _ in range(no_of_subjects):
    subject = input("Enter the name of subject: ")
    marks = float(input(f"Enter the marks of {subject}: "))
    marks_info[subject] = marks
    total_marks += marks
    
print("\n-----------------------")
print(f"Report Card for {name}")
print("-----------------------")

print(f"Total Marks: {total_marks}")

percentage = total_marks/no_of_subjects
print(f"Percentage: {percentage}%")
print("-----------------------")

if percentage >= 40:
    print("Congratulations! You are promoted to another class.")
else:
    print("Sorry, you have to appear next year.")
print("-----------------------")
