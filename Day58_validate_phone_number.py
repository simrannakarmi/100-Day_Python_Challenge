def check_phone_number(phone):
    if len(phone) != 10:
        return False
    elif not phone.isdigit():
        return False
    elif phone[0] not in "9":
        return False
    else:
        return True
        
phone = input("Enter phone number: ")
if check_phone_number(phone):
    print("Phone number is valid")
else:
    print("Phone number is invalid")
    