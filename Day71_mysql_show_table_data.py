import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="Password123", database="hundred_day")

if con.is_connected():
    q = "SELECT * FROM student"
    cur = con.cursor()
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        print("ID is",row[0]," Name is", row[1], " Age is",row[2])
    if cur.rowcount == 0:
        print("Table is Empty")
    else:
        print(cur.rowcount, " Students Processed")
else:
    print("Error in Connection")