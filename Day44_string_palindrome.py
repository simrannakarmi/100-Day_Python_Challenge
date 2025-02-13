text = input("Enter a String: ")
reverse = ""
n = len(text)


for i in range(0, n//2):
    # reverse += text[i]
    if text[i] != text[n-1]:
        print("It is not a Palindrome")
    n -= 1
    
    
    
if text == reverse:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome")
    