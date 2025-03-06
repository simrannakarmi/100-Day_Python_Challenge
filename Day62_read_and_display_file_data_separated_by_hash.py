f = open("story.txt", "r")
data = f.readlines()

print(data)

for line in data:
    # print("#".join(line.split()))
    for word in line.split():
        print(word, end="#")
f.close()