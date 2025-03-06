passwords = {"user": "python", "user1": "user1pass"}

for i in range(3):
    userid = input("Enter the User ID: ")
    passw = input("Enter the Password: ")
    
    if userid.lower() in passwords:
        if passw.lower() == passwords[userid]:
            print("Password Matched !!")
            print("Access Granted")
            break
else:
    print("Access Denied")
            