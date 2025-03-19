import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="Password123", database="hundred_day")

if con.is_connected():
    q = "SELECT * FROM student"
    cur = con.cursor()
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        print(row)
else:
    print("Error in Connection")