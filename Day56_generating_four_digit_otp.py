import random

def generate_otp():
    otp = []
    i = 0
    while i < 4:
        digit = random.randint(0, 9)
        if digit not in otp:
            otp.append(digit)
            i+=1
            
    return otp

otp = generate_otp()
print("Your OTP is: ", end=' ')
for i in otp:
    print(i, end=' ')
  