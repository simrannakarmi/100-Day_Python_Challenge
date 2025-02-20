def create(d_emp, n):
    for i in range(n):
        ename = input("Enter employee name: ")
        sal = int(input("Enter salary: "))
        job = input("Enter job: ")
        d_emp[ename] = [sal, job]
    
d_emp = {}
n = int(input("Enter the number of employees: "))
create(d_emp, n)
print("Employee Dictionary is: ",d_emp)
    