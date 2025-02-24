
def is_valid_email(email):
    if email.endswith(".com"):
        if email[0] != "a" and email.count("@") == 1 :
            for ch in email:
                if ch.isalpha() or ch.isdigit() or ch =="." or ch == "_" or ch == "@":
                    continue
                else:
                    return False
            else:
                return True
        else: 
            return False
    return False
    
email = input("Enter Email-ID: ")

if is_valid_email(email) :
    print("Valid Email id")
else:
    print("Not a valid Email id")    