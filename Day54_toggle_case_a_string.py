text = input("Enter a String: ")

result = ""

for ch in text:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
        
print("Original String:", text)
print("Swap Case String:", result)