import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Password123", database="hundred_day")

if con.is_connected():
    roll_num = input("Enter Roll No. of Student to be deleted: ")
    
    query1 = "SELECT * FROM student WHERE s_id="+roll_num
    cur = con.cursor()
    cur.execute(query1)
    res = cur.fetchall()
    for row in res:    
        print("Roll No.: ", row[0])
        print("Name: ", row[1])
        print("Age: ", row[2])
        
    choice = input("Are you sure you want to delete this student record (y/n): ")
    if choice.lower() in 'y, yes':
        q = "DELETE FROM student WHERE s_id="+roll_num
        cur.execute(q)
        con.commit()
        print("Student Data Deleted Successfully")