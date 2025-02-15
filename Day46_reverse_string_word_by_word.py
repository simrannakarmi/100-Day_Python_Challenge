text = input("Enter a String to be reversed: ")
words = text.split()
words = words[::-1]
result = ""
for w in words:
    result += w +" "
print(result)

