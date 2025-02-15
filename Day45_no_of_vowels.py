text = input("Enter a String: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1
        
print(f"The number of vowels in '{text}' is {count}.")        