def check_name(name):
    for ch in name:
        if not (ch.isalpha() or ch == ' '):
            return False
    else:
        return True

name = input("Enter your name to validate: ")
if check_name(name):
    print(name + " is a valid name")
else:
    print(name + " is not a valid name")
    