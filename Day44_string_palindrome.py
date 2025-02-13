text = input("Enter a String: ")
reverse = ""
n = len(text)
is_palindrome = True

for i in range(0, n//2):
    # reverse += text[i]
    if text[i] != text[n-1]:
       is_palindrome = False
    n -= 1
        
    
if is_palindrome:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome")
    