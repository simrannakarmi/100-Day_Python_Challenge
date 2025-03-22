import mysql.connector as mycon
con = mycon.connect(host="localhost", user="root", password="Password123", database="hundred_day")

if con.is_connected():
    search = input("Enter the Roll No. of the student: ")
    q = "SELECT * FROM student WHERE s_id=" + search
    cr = con.cursor()
    cr.execute(q)
    res = cr.fetchone()
    if res != None:
        print(res)
    else:
        print("No Student found with given ID")            