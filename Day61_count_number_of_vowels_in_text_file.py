f = open("story.txt", "r")
data = f.read()

vowels = 0

for ch in data:
    if ch in "aeiouAEIOU":
        vowels += 1

print(data)
print(f"No. of vowels in the file: {vowels}")

f.close()