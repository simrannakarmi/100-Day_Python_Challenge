password = input("Enter the required password: ")

n = len(password)

if n >= 8 and n <= 16:
    cap = 0
    small = 0
    digits = 0
    symbol = 0
    a = 0
    for ch in password:
        if ch.isupper():
            cap += 1
        elif ch.islower():
            small += 1
        elif ch.isdigit():
            digits += 1
        elif ch in ".,:!@#$%^&*()~?><":
            symbol += 1
        else:
            a += 1
            break
        
    if a != 0:
        print("Invalid Password")
    else:
        if cap > 0 and small > 0 and digits > 0 and symbol > 0:
            print("Password strength is strong")
        else:
            print("Weak Password")
else:
    print("Password must have minimum of 8 characters and maximum 16")