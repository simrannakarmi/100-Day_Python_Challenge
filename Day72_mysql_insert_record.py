import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Password123", database="hundred_day")

if con.is_connected():
    roll_num = int(input("Enter Roll No.: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    
    q = "INSERT INTO student VALUES (%s, %s, %s)"
    values = (roll_num, name, age)
    cur1 = con.cursor()
    cur1.execute(q, values)
    con.commit()
    print("Student Data Inserted Successfully.")
    