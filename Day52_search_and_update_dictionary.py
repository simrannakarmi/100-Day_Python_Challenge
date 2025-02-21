def create(d_emp, n):
    for i in range(n):
        ename = input("Enter employee name: ")
        sal = int(input("Enter salary: "))
        d_emp[ename] = sal
    
def search(d_emp, name):
    if name in d_emp:
        print("Current Salary is ", d_emp[name])
        d_emp[name] += d_emp[name] * 25/100
        print("Salary Updated!!!")
    else:
        print("No employee found with given name")
    
d_emp = {}

n = int(input("Enter the number of employees: "))
create(d_emp, n)
print("Employee Dictionary is: ",d_emp)

name = input("Enter Employee name whose salary has to be increased: ")
search(d_emp, name)
print("Employee Dictionary is: ",d_emp)
