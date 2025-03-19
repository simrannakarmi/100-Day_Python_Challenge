import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Password123", database="hundred_day")
if con.is_connected():
    roll_num = int(input("Enter Roll No.: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    
    q = "UPDATE student SET s_name=%s, age=%s WHERE s_id=%s"
    values = (name, age, roll_num)
    cur = con.cursor()
    cur.execute(q, values)
    con.commit()
    print("Student Data Updated Successfully")