import csv

username = input("Enter Username: ")
passw = input("Enter Password: ")

f = open("users.csv", "r")
data = csv.reader(f)
for row in data:
    if row[0] == username and row[1] == passw:
        print("Welcome,", username, " Access Granted")
        break
else:
    print("Invalid Username or Password.")
    print(username, passw)
    
f.close()
